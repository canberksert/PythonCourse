# [FUNCTIONS] Head-to-head total number of corners last game, 2 games before, 3 games before and average of those, when home team was home team and away team was away.
def func_H2H_TOT_CORNERS_HA_L1G(row):
    home = row['HomeTeam']
    away = row['AwayTeam']
    filtered_df = main[(main['HomeTeam']==home) & (main['AwayTeam']==away)]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].max()]
    try:
        return int(filtered_df['HC'].values)+int(filtered_df['AC'].values)
    except:
        return np.nan

def func_H2H_TOT_CORNERS_HA_L2G(row):
    home = row['HomeTeam']
    away = row['AwayTeam']
    filtered_df = main[(main['HomeTeam']==home) & (main['AwayTeam']==away)]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[1]['Date']]
        try:
            return int(filtered_df['HC'].values)+int(filtered_df['AC'].values)
        except:
            return np.nan
    except:
        return np.nan
    
def func_H2H_TOT_CORNERS_HA_L3G(row):
    home = row['HomeTeam']
    away = row['AwayTeam']
    filtered_df = main[(main['HomeTeam']==home) & (main['AwayTeam']==away)]
    filtered_df = filtered_df[filtered_df['Date']<row['Date']]
    try:
        filtered_df = filtered_df[filtered_df['Date']==filtered_df['Date'].sort_values(ascending=False).reset_index().loc[2]['Date']]
        try:
            return int(filtered_df['HC'].values)+int(filtered_df['AC'].values)
        except:
            return np.nan
    except:
        return np.nan