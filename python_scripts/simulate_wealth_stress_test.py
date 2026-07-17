import pandas as pd
import sqlite3

conn = sqlite3.connect('data/database/toronto_macro_wealth.db')
query = """
WITH credit_calc AS (
    -- Dynamically calculate the Debt Growth Index based on the new wide-format columns
    SELECT 
        REF_DATE,
        [Credit cards] AS National_Debt_Level,
        ([Credit cards] * 1.0 / FIRST_VALUE([Credit cards]) OVER (ORDER BY REF_DATE)) AS DEBT_GROWTH_INDEX
    FROM monthly_credit_liabilities
)
SELECT 
    w.[Age group],
    w.[Net worth (total assets less total debt)] AS Baseline_Wealth,
    c.REF_DATE,
    c.National_Debt_Level,
    ROUND(c.DEBT_GROWTH_INDEX, 4) AS DEBT_GROWTH_INDEX,
    -- Logic: Wealth gradually declines as debt grows beyond the baseline.
    ROUND(w.[Net worth (total assets less total debt)] * (
        1.0 - (
            CASE 
                -- 35–44: High vulnerability. Wealth declines by 30% of the debt growth rate.
                WHEN w.[Age group] = '35 to 44 years' THEN (c.DEBT_GROWTH_INDEX - 1.0) * 0.30
                
                -- 45–54: Moderate vulnerability. Apply a 15% penalty to debt growth.
                WHEN w.[Age group] = '45 to 54 years' THEN (c.DEBT_GROWTH_INDEX - 1.0) * 0.15
                
                -- 55–64: Low vulnerability. Reduce wealth by 5% of debt growth.
                WHEN w.[Age group] = '55 to 64 years' THEN (c.DEBT_GROWTH_INDEX - 1.0) * 0.05
                
                -- 65+: Highly insulated. Reduce wealth by 1% of debt growth.
                WHEN w.[Age group] = '65 years and older' THEN (c.DEBT_GROWTH_INDEX - 1.0) * 0.01
                
                ELSE 0
            END
        )
    ), 2) AS Adjusted_Wealth_Projection
FROM toronto_wealth_baseline w
CROSS JOIN credit_calc c
WHERE w.GEO = 'Toronto, Ontario'
AND w.Statistics = 'Median value for those holding asset or debt'
ORDER BY c.REF_DATE, w.[Age group];
"""
print("Running the stress test simulation...")

sim_df = pd.read_sql_query(query, conn)
conn.close()

output_file = 'data/outputs/stress_test_results.csv'
sim_df.to_csv(output_file, index=False)
print("The simulation results were successfully saved to stress_test_results.csv")