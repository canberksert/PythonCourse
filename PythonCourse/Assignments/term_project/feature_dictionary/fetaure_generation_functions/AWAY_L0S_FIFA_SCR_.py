def func_AWAY_L0S_FIFA_SCR_ATK(row):
    season = findSeason(row)
    return team_fifa_stats.loc[row['AwayTeam']]['ATT_'+season]

def func_AWAY_L0S_FIFA_SCR_ORT(row):
    season = findSeason(row)
    return team_fifa_stats.loc[row['AwayTeam']]['MID_'+season]

def func_AWAY_L0S_FIFA_SCR_DEF(row):
    season = findSeason(row)
    return team_fifa_stats.loc[row['AwayTeam']]['DEF_'+season]

def func_AWAY_L0S_FIFA_SCR_OVR(row):
    season = findSeason(row)
    return team_fifa_stats.loc[row['AwayTeam']]['OVR_'+season]