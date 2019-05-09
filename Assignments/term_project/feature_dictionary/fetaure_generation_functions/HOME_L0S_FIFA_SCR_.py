def func_HOME_L0S_FIFA_SCR_ATK(row):
    season = findSeason(row)
    return team_fifa_stats.loc[row['HomeTeam']]['ATT_'+season]

def func_HOME_L0S_FIFA_SCR_ORT(row):
    season = findSeason(row)
    return team_fifa_stats.loc[row['HomeTeam']]['MID_'+season]

def func_HOME_L0S_FIFA_SCR_DEF(row):
    season = findSeason(row)
    return team_fifa_stats.loc[row['HomeTeam']]['DEF_'+season]

def func_HOME_L0S_FIFA_SCR_OVR(row):
    season = findSeason(row)
    return team_fifa_stats.loc[row['HomeTeam']]['OVR_'+season]