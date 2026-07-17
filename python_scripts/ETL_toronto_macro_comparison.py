import pandas as pd

file_path = 'raw-data/toronto_wealth_and_debt_baseline_2023.csv' 
df = pd.read_csv(file_path)

target_geos = ['Canada', 'Toronto', 'Toronto, Ontario', 'Toronto (CMA)']
df_geo = df[df['GEO'].isin(target_geos)].copy()

target_ages = ['Under 35 years', '35 to 44 years', '45 to 54 years', '55 to 64 years', '65 years and older']
df_geo = df_geo[df_geo['Age group'].isin(target_ages)]

df_geo = df_geo[df_geo['Statistics'] == 'Median value for those holding asset or debt']

# Select required columns and remove unnecessary fields
columns_to_keep = ['REF_DATE', 'GEO', 'Age group', 'Assets and debts', 'VALUE']
df_clean = df_geo[columns_to_keep]

# Pivot Data: Convert from Long Format to Wide Format
df_pivot = df_clean.pivot_table(
    index=['REF_DATE', 'GEO', 'Age group'], 
    columns='Assets and debts', 
    values='VALUE', 
    aggfunc='sum'
).reset_index()

output_filename = 'data/processed/toronto_vs_canada_wealth_matrix.csv'
df_pivot.to_csv(output_filename, index=False)

print(f"Feature matrix exported successfully to:{output_filename}")
print(df_pivot.head())