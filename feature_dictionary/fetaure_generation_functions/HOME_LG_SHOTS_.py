# [FUNCTIONS] Home Team Last 1st 2nd 3rd Weeks' Shots
def func_HOME_LG_SHOTS_L1W(row):
    filtered_df = main[(main['HomeTeam']==row['HomeTeam']) | (main['AwayTeam']==row['HomeTeam'])]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].max()]
    try:
        if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
            return int(filtered_df['HS'].values)
        else:
            return int(filtered_df['AS'].values)
    except:
        return np.nan
    
def func_HOME_LG_SHOTS_L2W(row):
    filtered_df = main[(main['HomeTeam']==row['HomeTeam']) | (main['AwayTeam']==row['HomeTeam'])]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[1]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
                return int(filtered_df['HS'].values)
            else:
                return int(filtered_df['AS'].values)
        except:
            return np.nan
    except:
        return np.nan
    
def func_HOME_LG_SHOTS_L3W(row):
    filtered_df = main[(main['HomeTeam']==row['HomeTeam']) | (main['AwayTeam']==row['HomeTeam'])]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[2]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['HomeTeam']):
                return int(filtered_df['HS'].values)
            else:
                return int(filtered_df['AS'].values)
        except:
            return np.nan
    except:
        return np.nan