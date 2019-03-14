#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1. Import necessary libraries
import wbdata
import datetime
import pandas as pd

# Step 2. Retrieve abbreviations of South American countries
south_american_countries=['Venezuela', 'Uruguay', 'Suriname', 'Peru', 'Paraguay', 'Guyana', 'Ecuador', 'Colombia', 'Chile', 'Brazil', 'Bolivia', 'Argentina']
south_american_country_codes=[]
error_log=[]
for country in south_american_countries:
    temp = wbdata.search_countries(country,display=False)
    if len(temp)==1:
        south_american_country_codes.append(temp[0]['id'])
    else:
        error_log.append(country+': Either I could not find the country or there are more than one country with similar names.')
if (len(south_american_countries)==len(south_american_country_codes)):
    print('All of the countries parsed successfully.')
else:
    print('There were some errors. Please run print(error_log) to see errors.')       

# Step 3. Specify indicators
indicators = {'FP.CPI.TOTL.ZG':'3_inflation',
              'SP.POP.0014.TO.ZS': '0_control_children_population_percentage',
              'ccx_lf_pop_tot':'2_labor_force_participation_rate',
              'ccx_wka_pop_tot':'1_working_age_population_percentage',
              'per_nprog.overlap_pop_tot':'4_population_not_rec_social_protection',
              'SP.DYN.CBRT.IN': 'target_birth_rate'}

# Step 4. Extract data of Latin American countries
for country in south_american_country_codes:
    try:
        try: 
            temp_df=wbdata.get_dataframe(indicators, country=country, convert_date=True)
            df = pd.concat([df,temp_df],axis=0,sort=True)
        except: 
            df = wbdata.get_dataframe(indicators, country=country, convert_date=True)
    except:
        pass
df.to_csv('hw2_30223_oguzhan_akan_data.csv')

# Step 5. Import our regression file and run
import hw2_30223_oguzhan_akan_regression as src
regression_table, y, y_hat = src.manual_regression(path='hw2_30223_oguzhan_akan_data.csv',target='target_birth_rate', alpha=0.05)

regression_table
y
y_hat