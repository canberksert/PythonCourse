#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[5]:


# Read game-by-game data for each season
df1 = pd.read_csv('season-1314_csv.csv')
df2 = pd.read_csv('season-1415_csv.csv')
df3 = pd.read_csv('season-1516_csv.csv')
df4 = pd.read_csv('season-1617_csv.csv')
df5 = pd.read_csv('season-1718_csv.csv')

# Concatenate data frames and get rid of old ones
main = pd.concat([df1,df2,df3,df4,df5],axis=0)
del df1, df2, df3, df4, df5

# Create the target column which is the total number of corners in a game (e.g. Home Corners + Away Corners)
main['TARGET']=main.HC+main.AC
main.reset_index(inplace=True)


# In[6]:


teams_list = list(main.HomeTeam.unique())


# In[7]:


main.reset_index(inplace=True)


# In[8]:


# [FUNCTIONS] Home Team Last 1st 2nd 3rd Weeks' Goals
def func_HOME_LG_GOALS_L1W(row):
    filtered_df = main[(main['HomeTeam']==row['HomeTeam']) | (main['AwayTeam']==row['HomeTeam'])]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].max()]
    try:
        if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
            return int(filtered_df['FTHG'].values)
        else:
            return int(filtered_df['FTAG'].values)
    except:
        return np.nan
    
def func_HOME_LG_GOALS_L2W(row):
    filtered_df = main[(main['HomeTeam']==row['HomeTeam']) | (main['AwayTeam']==row['HomeTeam'])]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[1]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan
    
def func_HOME_LG_GOALS_L3W(row):
    filtered_df = main[(main['HomeTeam']==row['HomeTeam']) | (main['AwayTeam']==row['HomeTeam'])]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[2]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan


# In[9]:


# [FUNCTIONS] Home Team Last 1st 2nd 3rd Weeks' Goals
def func_HOME_LG_GOALS_H_L1W(row):
    filtered_df = main[main['HomeTeam']==row['HomeTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].max()]
    try:
        if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
            return int(filtered_df['FTHG'].values)
        else:
            return int(filtered_df['FTAG'].values)
    except:
        return np.nan
    
def func_HOME_LG_GOALS_H_L2W(row):
    filtered_df = main[main['HomeTeam']==row['HomeTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[1]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan
    
def func_HOME_LG_GOALS_H_L3W(row):
    filtered_df = main[main['HomeTeam']==row['HomeTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[2]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan


# In[18]:


# [FUNCTIONS] Home Team Last 1st 2nd 3rd Weeks' Goals
def func_HOME_LG_GOALS_A_L1W(row):
    filtered_df = main[main['AwayTeam']==row['HomeTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].max()]
    try:
        if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
            return int(filtered_df['FTHG'].values)
        else:
            return int(filtered_df['FTAG'].values)
    except:
        return np.nan
    
def func_HOME_LG_GOALS_A_L2W(row):
    filtered_df = main[main['AwayTeam']==row['HomeTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[1]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan
    
def func_HOME_LG_GOALS_A_L3W(row):
    filtered_df = main[main['AwayTeam']==row['HomeTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[2]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan


# In[11]:


# [FUNCTIONS] Away Team Last 1st 2nd 3rd Weeks' Goals
def func_AWAY_LG_GOALS_L1W(row):
    filtered_df = main[(main['HomeTeam']==row['AwayTeam']) | (main['AwayTeam']==row['AwayTeam'])]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].max()]
    try:
        if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
            return int(filtered_df['FTHG'].values)
        else:
            return int(filtered_df['FTAG'].values)
    except:
        return np.nan
    
def func_AWAY_LG_GOALS_L2W(row):
    filtered_df = main[(main['HomeTeam']==row['AwayTeam']) | (main['AwayTeam']==row['AwayTeam'])]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[1]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan
    
def func_AWAY_LG_GOALS_L3W(row):
    filtered_df = main[(main['HomeTeam']==row['AwayTeam']) | (main['AwayTeam']==row['AwayTeam'])]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[2]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan


# In[21]:


# [FUNCTIONS] Away Team Last 1st 2nd 3rd Weeks' Goals
def func_AWAY_LG_GOALS_H_L1W(row):
    filtered_df = main[main['HomeTeam']==row['AwayTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].max()]
    try:
        if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
            return int(filtered_df['FTHG'].values)
        else:
            return int(filtered_df['FTAG'].values)
    except:
        return np.nan
    
def func_AWAY_LG_GOALS_H_L2W(row):
    filtered_df = main[main['HomeTeam']==row['AwayTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[1]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan
    
def func_AWAY_LG_GOALS_H_L3W(row):
    filtered_df = main[main['HomeTeam']==row['AwayTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[2]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan


# In[22]:


# [FUNCTIONS] Away Team Last 1st 2nd 3rd Weeks' Goals
def func_AWAY_LG_GOALS_A_L1W(row):
    filtered_df = main[main['AwayTeam']==row['AwayTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].max()]
    try:
        if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
            return int(filtered_df['FTHG'].values)
        else:
            return int(filtered_df['FTAG'].values)
    except:
        return np.nan
    
def func_AWAY_LG_GOALS_A_L2W(row):
    filtered_df = main[main['AwayTeam']==row['AwayTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[1]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan
    
def func_AWAY_LG_GOALS_A_L3W(row):
    filtered_df = main[main['AwayTeam']==row['AwayTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[2]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
                return int(filtered_df['FTHG'].values)
            else:
                return int(filtered_df['FTAG'].values)
        except:
            return np.nan
    except:
        return np.nan


# In[12]:


final_df = main.copy()


# In[13]:


final_df['HOME_LG_GOALS_L1W']=final_df.apply(func_HOME_LG_GOALS_L1W,axis=1)
final_df['HOME_LG_GOALS_L2W']=final_df.apply(func_HOME_LG_GOALS_L2W,axis=1)
final_df['HOME_LG_GOALS_L3W']=final_df.apply(func_HOME_LG_GOALS_L3W,axis=1)
final_df['HOME_LG_GOALS_L3W_COMB']=final_df.HOME_LG_GOALS_L1W+final_df.HOME_LG_GOALS_L2W+final_df.HOME_LG_GOALS_L3W


# In[14]:


final_df['HOME_LG_GOALS_H_L1W']=final_df.apply(func_HOME_LG_GOALS_H_L1W,axis=1)
final_df['HOME_LG_GOALS_H_L2W']=final_df.apply(func_HOME_LG_GOALS_H_L2W,axis=1)
final_df['HOME_LG_GOALS_H_L3W']=final_df.apply(func_HOME_LG_GOALS_H_L3W,axis=1)
final_df['HOME_LG_GOALS_H_L3W_COMB']=final_df.HOME_LG_GOALS_H_L1W+final_df.HOME_LG_GOALS_H_L2W+final_df.HOME_LG_GOALS_H_L3W


# In[19]:


final_df['HOME_LG_GOALS_A_L1W']=final_df.apply(func_HOME_LG_GOALS_A_L1W,axis=1)
final_df['HOME_LG_GOALS_A_L2W']=final_df.apply(func_HOME_LG_GOALS_A_L2W,axis=1)
final_df['HOME_LG_GOALS_A_L3W']=final_df.apply(func_HOME_LG_GOALS_A_L3W,axis=1)
final_df['HOME_LG_GOALS_A_L3W_COMB']=final_df.HOME_LG_GOALS_A_L1W+final_df.HOME_LG_GOALS_A_L2W+final_df.HOME_LG_GOALS_A_L3W


# In[16]:


final_df['AWAY_LG_GOALS_L1W']=final_df.apply(func_AWAY_LG_GOALS_L1W,axis=1)
final_df['AWAY_LG_GOALS_L2W']=final_df.apply(func_AWAY_LG_GOALS_L2W,axis=1)
final_df['AWAY_LG_GOALS_L3W']=final_df.apply(func_AWAY_LG_GOALS_L3W,axis=1)
final_df['AWAY_LG_GOALS_L3W_COMB']=final_df.AWAY_LG_GOALS_L1W+final_df.AWAY_LG_GOALS_L2W+final_df.AWAY_LG_GOALS_L3W


# In[23]:


final_df['AWAY_LG_GOALS_H_L1W']=final_df.apply(func_AWAY_LG_GOALS_H_L1W,axis=1)
final_df['AWAY_LG_GOALS_H_L2W']=final_df.apply(func_AWAY_LG_GOALS_H_L2W,axis=1)
final_df['AWAY_LG_GOALS_H_L3W']=final_df.apply(func_AWAY_LG_GOALS_H_L3W,axis=1)
final_df['AWAY_LG_GOALS_H_L3W_COMB']=final_df.AWAY_LG_GOALS_H_L1W+final_df.AWAY_LG_GOALS_H_L2W+final_df.AWAY_LG_GOALS_H_L3W


# In[24]:


final_df['AWAY_LG_GOALS_A_L1W']=final_df.apply(func_AWAY_LG_GOALS_A_L1W,axis=1)
final_df['AWAY_LG_GOALS_A_L2W']=final_df.apply(func_AWAY_LG_GOALS_A_L2W,axis=1)
final_df['AWAY_LG_GOALS_A_L3W']=final_df.apply(func_AWAY_LG_GOALS_A_L3W,axis=1)
final_df['AWAY_LG_GOALS_A_L3W_COMB']=final_df.AWAY_LG_GOALS_A_L1W+final_df.AWAY_LG_GOALS_A_L2W+final_df.AWAY_LG_GOALS_A_L3W


# In[25]:


final_df.to_excel('test1.xlsx')

