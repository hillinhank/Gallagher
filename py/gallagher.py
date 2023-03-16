import pandas as pd
filepath = '/Users/user/Desktop/Gallagher/Utilization_and_Costs_of_Health_Services_for_Medicare_Fee-for-Service_Beneficiaries__Washington_State_and_Counties__2007-2018.csv'

g_data = pd.read_csv(filepath)
g_data.head()

df_grouped = g_data.groupby('Year')
df_2009 = df_grouped.get_group(2009)
df_2014 = df_grouped.get_group(2014)
df_2014.head()


keep_cols = ['County', '(To sort by county and year)','(To sort by year and county)','Year', 'State and County FIPS Code'] + [col for col in df_2009.columns if 'OP' in col or 'IP' in col]
df2009 = df_2009.loc[:, keep_cols]
df2009.to_excel("cleaned_2009.xlsx")


keep_cols = ['County', '(To sort by county and year)','(To sort by year and county)','Year', 'State and County FIPS Code'] + [col for col in df_2014.columns if 'OP' in col or 'IP' in col]
df2014 = df_2014.loc[:, keep_cols]
df2014.to_excel("cleaned_2014.xlsx")

