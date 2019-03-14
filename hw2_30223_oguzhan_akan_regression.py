#!/usr/bin/env python
# coding: utf-8

# In[1]:


def manual_regression(path='data.csv',target='target', alpha=0.05):
    # Step 0. Import libraries and read the data
    import pandas as pd
    import numpy as np
    from numpy.linalg import inv
    from scipy.stats import t
    import matplotlib.pyplot as plt
    
    def read_data(path, target):
        try:
            df = pd.read_csv(path,sep=',')
            return df
        except TypeError:
            print('Data import unsuccessful, please make sure you have your data in csv format.')

    # Step 1. Listwise deletion of Null values
    def handle_na(df):
        na_rows = []
        for row in df.index:
            if(len(df.isna().iloc[row].unique())==2):
                na_rows.append(row)
        return df.drop(na_rows)

    # Step 2. Retrieve regression estimates
    def findEstimates(df, target, alpha=alpha):
        X = df.drop([target,'date'],axis=1).values
        n = X.shape[0]
        k = X.shape[1]
        X = np.concatenate((np.ones([n,1]),X),axis=1)
        y = df[target].values
        beta = (inv(X.T @ X ) @ X.T) @ y
        y_hat = np.sum(X*beta,axis=1)
        e = y - y_hat
        std_sq = (e.T @ e)/(n-k-1)
        var_beta = std_sq * inv(X.T @ X )
        standard_error = np.sqrt(np.diag(var_beta))
        lower = beta - t.ppf(1 - alpha, df=n-k-1) * standard_error
        upper = beta + t.ppf(1 - alpha, df=n-k-1) * standard_error
        regression_table = pd.DataFrame(columns = ['Estimate','Std. Error','Lower','Upper'], 
                                        index=['(Constant)']+[e for e in df.columns if e not in [target,'date']])
        regression_table['Estimate'] = beta
        regression_table['Std. Error'] = standard_error
        regression_table['Lower'] = lower
        regression_table['Upper'] = upper
        return regression_table, y, y_hat

    # Step 3. Functions necessary for regression
    df = read_data(path,target)
    df = handle_na(df)

    # Step 4. Draw plots for each feature versus target variable
    def draw_plot(df):
        for feat in [e for e in df.columns if e not in [target,'date']]:
            x = df[feat]
            y = df[target]
            fig = plt.figure()
            plt.xlabel(feat)
            plt.ylabel(target)
            plt.suptitle(feat)
            plt.scatter(x, y, alpha=1,marker='.')
            fig.savefig(feat+'.png', dpi=100)
            
    draw_plot(df)        
    return findEstimates(df,target)

