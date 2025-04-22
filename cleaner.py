import pandas as pd

df=pd.read_csv('./dataset/world-education-data.csv')

print(df.info())
print(df.describe())
# print(df.head())
df['gov_exp_pct_gdp']= df['gov_exp_pct_gdp'].fillna(df['gov_exp_pct_gdp'].mean())
df['lit_rate_adult_pct']= df['lit_rate_adult_pct'].fillna(df['lit_rate_adult_pct'].mean())
df['pri_comp_rate_pct']= df['pri_comp_rate_pct'].fillna(df['pri_comp_rate_pct'].mean())
df['pupil_teacher_primary']=df['pupil_teacher_primary'].fillna(df['pupil_teacher_primary'].mean())
df['pupil_teacher_secondary']=df['pupil_teacher_secondary'].fillna(df['pupil_teacher_secondary'].mean())
df['school_enrol_primary_pct']=df['school_enrol_primary_pct'].fillna(df['school_enrol_primary_pct'].mean())
df['school_enrol_secondary_pct']=df['school_enrol_secondary_pct'].fillna(df['school_enrol_secondary_pct'].mean())
df['school_enrol_tertiary_pct']=df['school_enrol_tertiary_pct'].fillna(df['school_enrol_tertiary_pct'].mean())

print(df.isnull().sum())
df.to_csv('./dataset/world-education-data-cleaned.csv', index=False, float_format='%.4f')
print(df.info())
