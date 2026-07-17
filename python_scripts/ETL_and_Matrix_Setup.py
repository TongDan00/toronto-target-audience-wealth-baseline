import pandas as pd
import os
import numpy as np

def process_wealth_baseline():
    input_file = 'raw-data/toronto_wealth_and_debt_baseline_2023.csv'
    output_dir = 'data/processed'
    output_file = f'{output_dir}/toronto_wealth_matrix_2023.csv'

    os.makedirs(output_dir, exist_ok=True)

    print(f"Reading file: {input_file}...")
    
    if not os.path.exists(input_file):
        print(f"Error: File not found. Please ensure the file is placed at:{input_file}")
        return

    try:
       # Remove dynamic metadata header rows from Statistics Canada source files
        skip_lines = 0
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f):
                if '"GEO"' in line or 'GEO,' in line or 'REF_DATE' in line or 'Age group' in line:
                    skip_lines = i
                    break
        
        if skip_lines > 0:
            print(f"Statistics Canada metadata detected. Skipping the first {skip_lines} rows before processing...")
            
        df = pd.read_csv(input_file, skiprows=skip_lines)
        print(f"Successfully read! Raw data size: {df.shape[0]} rows, {df.shape[1]} columns")
        
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # Standardize columns and include SCALAR_FACTOR to capture hidden unit multipliers
    core_cols = [col for col in df.columns if col in ['REF_DATE', 'GEO', 'Age group', 'Assets and debts', 'Statistics', 'VALUE', 'SCALAR_FACTOR']]
    
    if len(core_cols) < 4:
        print("Warning: Expected core columns not found, please check the CSV file content.")
        return
        
    df_clean = df[core_cols].copy()

    # Use string matching to capture bilingual Statistics Canada labels (e.g., "All ages")
    if 'Age group' in df_clean.columns:
        df_clean = df_clean[~df_clean['Age group'].str.contains('All ages', case=False, na=False)]
        
    # Convert VALUE to numeric format and replace missing values with 0
    if 'VALUE' in df_clean.columns:
        df_clean['VALUE'] = pd.to_numeric(df_clean['VALUE'], errors='coerce').fillna(0) 

    # Apply SCALAR_FACTOR multiplier before pivoting to ensure accurate values
    if 'SCALAR_FACTOR' in df_clean.columns:
        multiplier_map = {'millions': 1000000, 'thousands': 1000, 'units': 1}
        # Map SCALAR_FACTOR multipliers, defaulting to 1 when no valid factor is found
        df_clean['MULTIPLIER'] = df_clean['SCALAR_FACTOR'].map(multiplier_map).fillna(1)
        df_clean['VALUE'] = df_clean['VALUE'] * df_clean['MULTIPLIER']
        # Remove SCALAR_FACTOR columns after value scaling, as they are no longer needed for pivoting
        df_clean.drop(columns=['SCALAR_FACTOR', 'MULTIPLIER'], inplace=True)

    # Pivot long-format data into a feature matrix
    print("\nPivoting data into a business feature matrix...")
    try:
        df_matrix = df_clean.pivot_table(
            index=['GEO', 'Age group', 'Statistics'], 
            columns='Assets and debts', 
            values='VALUE',
            aggfunc='first' 
        ).reset_index()

        df_matrix.columns.name = None

        print("\nData reshaping completed successfully. Preview of the demographic feature matrix:")
        pd.set_option('display.max_columns', None)
        print(df_matrix.head())

        df_matrix.to_csv(output_file, index=False)
        print(f"\nCleaned feature matrix saved successfully to:{output_file}")

    except KeyError as e:
        print(f"\nError during data reshaping. Expected column not found: {e}")

process_wealth_baseline()