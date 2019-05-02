# [FUNCTIONS] Away Team Last 1st 2nd 3rd Weeks' Goals
def func_AWAY_LG_SHOTS_OT_H_L1W(row):
    filtered_df = main[main['HomeTeam']==row['AwayTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].max()]
    try:
        if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
            return int(filtered_df['HST'].values)
        else:
            return int(filtered_df['AST'].values)
    except:
        return np.nan
    
def func_AWAY_LG_SHOTS_OT_H_L2W(row):
    filtered_df = main[main['HomeTeam']==row['AwayTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[1]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
                return int(filtered_df['HST'].values)
            else:
                return int(filtered_df['AST'].values)
        except:
            return np.nan
    except:
        return np.nan
    
def func_AWAY_LG_SHOTS_OT_H_L3W(row):
    filtered_df = main[main['HomeTeam']==row['AwayTeam']]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[2]['Date']]
        try:
            if(filtered_df.iloc[0]['HomeTeam']==row['AwayTeam']):
                return int(filtered_df['HST'].values)
            else:
                return int(filtered_df['AST'].values)
        except:
            return np.nan
    except:
        return np.nan
