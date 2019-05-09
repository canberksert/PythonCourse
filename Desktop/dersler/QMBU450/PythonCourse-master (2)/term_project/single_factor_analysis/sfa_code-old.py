#!/usr/bin/env python
# coding: utf-8

# In[ ]:


total_stats = pd.DataFrame(columns=['# of null', '% of null', 'PD of null', 'org c-value', 'ranked c-value', 'iv', 'min_val','max_val','use','null treat','discretization','reason','checked by','date'])
feature_name = list()
cont_cat = list()
min_val = list()
max_val = list()
def univar(df, feature):
    univ_stats = df[feature].describe(percentiles=[.01,.05,.10,.90,.95,.99])
    min_val = univ_stats.loc['5%']
    max_val = univ_stats.loc['95%']
    return min_val, max_val

def cutdata(df, feature, target, min_val, max_val):
    cut_df = main[['TALEP_NO',feature,target]].copy()
    cut_df['ResearchVar'] = np.where(cut_df[feature].isnull(), cut_df[feature], 
                                     np.where(cut_df[feature]<min_val, min_val, 
                                              np.where(cut_df[feature]>max_val, max_val, cut_df[feature])))
    return cut_df

def ranking(df, rank_num, feature='ResearchVar'):
    # create dataframes for null and notnull values separately
    nnull_data = df[~df[feature].isnull()].copy()
    null_data = df[df[feature].isnull()].copy()
    
    # get count of notnull dataframe
    count = nnull_data[feature].count()
    print('Number of not-null observations: '+str(count))
    
    rankeddata = pd.DataFrame()
    # sort not-null dataframe according to feature and assign initial ranking
    rankeddata = nnull_data.sort_values(by=feature)
    rankeddata = rankeddata.reset_index().drop(['index'],axis=1)
    rankeddata = rankeddata.join(pd.DataFrame(list(range(1,count+1)),columns=['rownum']))
    rankeddata['init_rank'] = (rankeddata['rownum']*rank_num/(count+1)).astype('int')
    
    # assign the same rank to same values
    rank_gr = rankeddata[[feature,'init_rank']].groupby(feature).mean().reset_index()
    rank_gr['RankVar'] = np.round(rank_gr['init_rank'], 0).astype('int')
    rank_gr = rank_gr.drop(['init_rank'],axis=1)
    rankeddata = rankeddata.merge(rank_gr, on=feature)
    rankeddata = rankeddata.drop(['rownum','init_rank'], axis=1)
    
    # append null data
    null_data['RankVar'] = None
    rankeddata = rankeddata.append(null_data,sort=False)
    return rankeddata

def graph_table(df, target='M6_F', feature='RankVar'):
    # create dataframes for null and notnull values separately
    nnull_data = df[~df[feature].isnull()].copy()
    null_data = df[df[feature].isnull()].copy()
    
    # min, max, mean values for ranks
    pv1 = nnull_data.pivot_table(values='ResearchVar', index=feature, aggfunc=('mean','min','max'))
    pv1.columns = ['max_rank_value','mean_rank_value','min_rank_value']
    
    # % of total data
    pv2 = df.pivot_table(values='TALEP_NO',index='RankVar', aggfunc = 'count')
    pv2.columns = ['count_of_rank']
    sum_adet = pv2.sum(axis=0)['count_of_rank']
    pv2['pc_of_rank'] = pv2['count_of_rank']/sum_adet
    
    # FPD Ratio
    pv3 = nnull_data.pivot_table(values=target, index='RankVar', aggfunc='mean')
    pv3.columns = ['fpd_ratio']
    
    # join pivots
    pv = pv1.join(pv2.join(pv3))
    
    return pv

def null_stats(df, target='M6_F', org_feature='ResearchVar'):
    null_data = df[df[org_feature].isnull()].copy()
    null_adet = null_data['TALEP_NO'].count()
    total_adet = df['TALEP_NO'].count()
    nmiss_pc = null_adet/total_adet
    if(null_adet==0 or null_data.gropby('M6_F').count().index.tolist()==[0]):
        null_pd = 0
    else:
        null_pd = null_data.groupby('M6_F').count()['TALEP_NO'].loc[1]/null_data.groupby('M6_F').count()['TALEP_NO'].sum()
    return null_adet, nmiss_pc, null_pd

def c_value(df, target='M6_F', org_feature='ResearchVar', rank_feature='RankVar'):
    nnull_data = df[~df[org_feature].isnull()].copy()
    c_org = 1
    c_ranked = 2
    if c_org <= 0.5:
        c_org = 1-c_org
    if c_ranked <= 0.5:
        c_ranked = 1-c_ranked
    return c_org, c_ranked

def information_value(df, target='M6_F', org_feature='ResearchVar', rank_feature ='RankVar', rank_null_tr=-1):
    return 1

def stats_calc(df, target='M6_F', org_feature='ResearchVar', rank_feature='RankVar', rank_null_tr=-1):
    null_adet, nmiss_pc, null_pd = null_stats(df, target=target, org_feature='ResearchVar')
    c_org, c_ranked = c_value(df, target=target, org_feature='ResearchVar', rank_feature = 'RankVar')
    iv = information_value(df, target=target, org_feature='ResearchVar', rank_feature ='RankVar')
    stats_df = pd.DataFrame([[null_adet,nmiss_pc,null_pd,c_org,c_ranked,iv]], columns=['# of null', '% of null', 'PD of null','org c-value','ranked c-value', 'iv'])
    return stats_df

def sfa_cont(df, feature,target,rank_num):
    min_val, max_val = univar(df, feature)
    cut_df = cutdata(df,feature,target,min_val,max_val)
    rankeddata=ranking(cut_df,rank_num)
    stats_df = stats_calc(df=rankeddata, target=target, org_feature='ResearchVar',rank_feature='RankVar', rank_null_tr=-1)
    graph_stats = graph_table(rankeddata, target=target, feature='RankVar')
    return graph_stats, stats_df, min(df[feature]), max(df[feature])

# SFA CONTINOUS VARIABLES END #

def graph_table_cat(df, target='M6_F', feature='ResearchVar'):
    # create dataframes for null and notnull values separately
    nnull_data = df[~df[feature].isnull()].copy()
    all_data = df.copy()
    all_data.reset_index(inplace=True)
    all_data[feature]=all_data[feature].replace(np.nan,'Null')
    all_data.set_index(feature,inplace=True)
    
    count=nnull_data[feature].count()
    
    # FPD%
    pv1 = all_data.pivot_table(values=target,index=feature,aggfunc='mean')
    pv1.columns= ['fpd_ratio']
    
    # % of total data
    pv2 = all_data.pivot_table(values='TALEP_NO', index=feature,aggfunc='count')
    pv2.columns = ['count_of_rank']
    sum_adet = pv2.sum(axis=0)['count_of_rank']
    pv2['pc_of_rank']=pv2['count_of_rank']/sum_adet
    
    pv=pv1.join(pv2)
    
    return pv
    
    
def null_stats_cat(df, target='M6_F', org_feature='ResearchVar'):
    null_data=df[df[org_feature].isnull()].copy()
    null_adet=null_data['TALEP_NO'].count()
    total_adet = df['TALEP_NO'].count()
    nmiss_pc = null_adet/total_adet
    try:
        null_pd = null_data.groupby('M6_F').count()['TALEP_NO'].loc[1]/null_data.groupby('M6_F').count()['TALEP_NO'].sum()
    except KeyError:
        null_pd=0
        
    return null_adet, nmiss_pc, null_pd

def information_value_cat(df, target='M6_F', org_feature='ResearchVar', rank_null_tr=-1):
    tr_data = df.copy()
    tr_data[rank_feature] = tr_data[rank_feature].fillna(rank_null_tr)
    
    pv = tr_data.pivot_table(values='TALEP_NO', index=org_feature, columns=target,aggfunc='count')
    pv.columns=['good','bad']
    num_good = pv.sum(axis=0)['good']
    num_bad = pv.sum(axis=0)['bad']
    
    pv['pc_good'] = pv['good']/num_good
    pv['pc_bad'] = pv['bad']/num_bad
    
    pv['woe']=np.log(pv['pc_good']/pv['pc_bad'])
    pv['iv'] = (pv['pc_good'] - pv['pc_bad']) * pv['woe']
    iv = pv['iv'].sum()
    return iv
    
def stats_calc_cat(df, target, org_feature, rank_null_tr = -1):
    null_adet,nmiss_pc,null_pd = null_stats_cat(df,target,org_feature)
    iv = calc_iv(df,target,org_feature,rank_null_tr)
    stats_df = pd.DataFrame([[null_adet,nmiss_pc,null_pd, iv]],columns=['# of null','% of null','PD of null', 'iv'])
    return stats_df

def sfa_cat(df, feature,target):
    stats_df = stats_calc_cat(df = df, target='M6_F', org_feature=feature, rank_null_tr = -1)
    graph_stats = graph_table_cat(df,target='M6_F',feature=feature)
    return graph_stats, stats_df
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

