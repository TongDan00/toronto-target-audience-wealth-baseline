import pandas as pd
import sqlite3

print("Loading processed macroeconomic feature matrices...")

credit_df = pd.read_csv('data/processed/monthly_credit_matrix_2023_2026.csv')
interest_df = pd.read_csv('data/processed/monthly_interest_rate_matrix_2023_2026.csv')
cpi_df = pd.read_csv('data/processed/monthly_cpi_matrix_2023_2026.csv')
wealth_df = pd.read_csv('data/processed/toronto_wealth_matrix_2023.csv')

print("Merging data on 'REF_DATE'...")

# Merge datasets by matching Month and Year (REF_DATE)
master_df = pd.merge(credit_df, interest_df, on='REF_DATE', how='inner')
master_df = pd.merge(master_df, cpi_df, on='REF_DATE', how='inner')

# Save Integrated Dataset to SQLite Database 
db_path = 'data/database/toronto_macro_wealth.db'
print(f"Connecting to database: {db_path}...")
conn = sqlite3.connect(db_path)

print("Writing tables to SQLite database...")
master_df.to_sql('master_macroeconomic_matrix', conn, if_exists='replace', index=False)
wealth_df.to_sql('toronto_wealth_baseline', conn, if_exists='replace', index=False)
credit_df.to_sql('monthly_credit_liabilities', conn, if_exists='replace', index=False)

conn.close()
print("SQLite tables created successfully.")

# Export dataset for Tableau analysis
output_file = 'data/processed/master_macroeconomic_matrix.csv'
master_df.to_csv(output_file, index=False)
print(f"Tableau CSV export completed successfully: {output_file}")