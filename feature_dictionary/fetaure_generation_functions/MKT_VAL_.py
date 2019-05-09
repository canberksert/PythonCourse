def findSeason(row):
    year = int(row['Date'][:4])
    month = int(row['Date'][5:7])
    if(month>5):
        return str(year)+str(year+1)
    else:
        return str(year-1)+str(year)
    
def func_HOME_MKT_VAL(row):
    season = findSeason(row)
    return team_values.loc[row['HomeTeam']][season]

def func_AWAY_MKT_VAL(row):
    season = findSeason(row)
    return team_values.loc[row['AwayTeam']][season]