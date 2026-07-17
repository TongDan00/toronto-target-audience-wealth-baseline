# Navigating the 2028 Mortgage Renewal Challenge: Toronto Household Debt & Liquidity Analysis

[![Dashboard Preview](macro_overview.png)](https://public.tableau.com/shared/ZRHSCQX7D?:display_count=n&:origin=viz_share_link)

Hi, I'm Yu-Tong Lin. With a background in Industrial Engineering and Business Management, combined with experience in operational planning and data analytics, I approach data through both a technical and operational lens. I focus not only on identifying trends but also on uncovering operational bottlenecks, business risks, and opportunities for data-driven decision-making.

Living in Toronto, I wanted to build an end-to-end analytics pipeline addressing a major Canadian economic challenge: the large-scale mortgage renewal cycle expected in the coming years and its potential impact on household cash flow and consumer liquidity.

## The Business Case

High-level economic indicators can often hide important differences between regions and demographic groups. While national-level data may suggest that households are adapting to higher interest rates, localized analysis can reveal specific segments experiencing higher financial pressure.

This project analyzes mortgage debt exposure across age groups and geographic markets, with a focus on Toronto's under-45 demographic. The analysis highlights differences in mortgage leverage compared with national benchmarks and explores potential liquidity risks associated with future mortgage renewals.

For financial institutions, these insights represent more than an economic trend. They provide a data-driven opportunity to improve customer segmentation, prioritize retention strategies, and develop proactive financial solutions such as refinancing support, debt restructuring, and liquidity-focused products.

## 💡 Strategic Business Recommendations
Based on the macroeconomic analysis and household debt trends, financial institutions can proactively adjust their retail banking strategies to better support customers during the mortgage renewal cycle.

*   **Prioritize Higher-Leverage Customers:** Focus outreach on homeowners under 45, who exhibit higher mortgage leverage than national benchmarks. Tailored solutions such as debt consolidation, refinancing, and Home Equity Lines of Credit (HELOCs) may help reduce financial pressure during mortgage renewals.
*   **Strengthen Customer Retention:** Rebalance branch advisory resources toward customer retention and proactive financial planning. Supporting existing customers through refinancing discussions, debt management, and renewal planning can strengthen long-term relationships while reducing portfolio risk.
*   **Encourage Long-Term Financial Resilience:** Expand accessible savings and investment tools, such as round-up savings and automated micro-investing, to help customers gradually build emergency funds and improve long-term financial resilience.

---

## 📊 Dashboard Highlights
The Tableau dashboard identifies two demographic segments with distinct financial characteristics.
[![Dashboard Preview](toronto_deep_dive.png)](https://public.tableau.com/shared/ZRHSCQX7D?:display_count=n&:origin=viz_share_link)

### Cash Flow Pressure Segment (Ages 35–44)
*   **Visual Cue:** Highlighted by the steep decline in the projected wealth trajectory.
*   **Key Insight:** Households in this age group generally carry higher mortgage balances and may be more sensitive to changes in borrowing costs during future mortgage renewals.
*   **Potential Business Opportunity:** Provide proactive refinancing guidance, debt consolidation options, and personalized financial planning to support customers through the renewal cycle.

### Asset Preservation Segment (Ages 65+)
*   **Visual Cue:** Represented by the relatively stable wealth trajectory for older households.
*   **Key Insight:** This demographic typically exhibits lower debt exposure and stronger asset positions, making their financial profiles less sensitive to interest rate changes.
*   **Potential Business Opportunity:** Focus on wealth preservation strategies, retirement planning, Cashable GICs, TFSAs, and other investment solutions aligned with long-term financial goals.

## Data Architecture

```text
Statistics Canada CSV Files
          ↓
Python ETL Pipeline
          ↓
SQLite Master Macroeconomic Table
          ↓
Tableau Executive Dashboard
          ↓
Business Recommendations
```

## Tech Stack

**Data Engineering**

* Python (Pandas) for data extraction, cleaning, transformation, and integration
* SQLite for storing the integrated master macroeconomic dataset
* ETL pipeline design for processing Statistics Canada datasets

**Data Visualization**

* Tableau for interactive executive dashboards
* Custom navigation design for non-technical stakeholders

**Analytics Methods**

* Time-series analysis
* Demographic segmentation
* Debt exposure analysis
* Business scenario evaluation

## Project Workflow

The pipeline transforms raw public datasets into actionable business insights:

1. Extract economic and demographic datasets from Statistics Canada
2. Clean and standardize inconsistent source formats
3. Apply data validation and transformation rules
4. Build integrated macroeconomic feature matrices
5. Visualize trends through Tableau dashboards
6. Translate findings into operational recommendations


```
## Project Structure & Analytics Workflow
This repository is structured to guide users from raw macroeconomic extraction to a localized, 180-day business insight simulation.

toronto-target-audience-wealth-baseline/
│
├── data/                                   # Centralized data storage
│   ├── database/                           # SQLite database storage
│   │   └── toronto_macro_wealth.db         # Master database for the 180-day simulation
│   ├── outputs/                            # Final simulation outputs
│   │   └── stress_test_results.csv         # Final 180-day liquidity simulation output
│   └── processed/                          # Cleaned, "wide-format" matrices ready for Tableau
│       ├── master_macroeconomic_matrix.csv
│       ├── monthly_cpi_matrix_2023_2026.csv
│       ├── monthly_credit_matrix_2023_2026.csv
│       ├── monthly_interest_rate_matrix_2023_2026.csv
│       ├── toronto_vs_canada_wealth_matrix.csv
│       └── toronto_wealth_matrix_2023.csv
│
├── python_scripts/                         # Modular ETL and analytics pipeline
│   ├── clean_cpi.py                        # Standardizes Consumer Price Index features
│   ├── clean_credit_liabilities.py         # Standardizes national credit metrics
│   ├── clean_interest_rates.py             # Formats Bank of Canada target rates
│   ├── ETL_and_Matrix_Setup.py             # Initializes pipeline and core matrices
│   ├── ETL_toronto_macro_comparison.py     # Executes long-to-wide format transformation
│   ├── merge_macro_master.py               # Joins all datasets into the master SQLite table
│   └── simulate_wealth_stress_test.py      # Business logic for the 180-day cash flow bottleneck test
│
├── raw-data/                               # Untouched Statistics Canada baseline files
│   ├── monthly_cpi_2023_2026.csv
│   ├── monthly_credit_liabilities_2023_2026.csv
│   ├── monthly_interest_rate_2023_2026.csv
│   └── toronto_wealth_and_debt_baseline_2023.csv
│
├── README.md                               # Project documentation and business insights
└── requirements.txt                        # Python dependencies (pandas)
```

## 📁 Data Sources
The foundational data for this project is sourced from publicly available datasets published by Statistics Canada.
*   **Wealth Baseline:** [Assets and debts held by economic family type, by age group](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110001601)> **Note:** This dataset serves as the primary baseline for the Python-based wealth stress test simulation.
*   **Income Baseline:** [Income of individuals by age group, gender and income source](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110023901)
*   **Consumer Price Index (CPI):** [Consumer Price Index by product group, monthly, percentage change](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000413)
*   **Interest Rates:** [Financial market statistics, last Wednesday unless otherwise stated, Bank of Canada](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1010012201)
*   **Credit Liabilities:** [Distributions of household economic accounts, wealth, by characteristic](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610063901)

