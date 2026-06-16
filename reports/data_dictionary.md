# Data Dictionary

## 01_fund_master.csv

| Column Name | Data Type | Business Definition | Source |
|-------------|------------|---------------------|---------|
| amfi_code | Integer | Unique AMFI scheme code | fund_master.csv |
| scheme_name | Text | Name of mutual fund scheme | fund_master.csv |
| fund_house | Text | Asset management company | fund_master.csv |
| category | Text | Scheme category | fund_master.csv |

## 02_nav_history.csv

| Column Name | Data Type | Business Definition | Source |
|-------------|------------|---------------------|---------|
| amfi_code | Integer | Scheme identifier | nav_history.csv |
| date | Date | NAV date | nav_history.csv |
| nav | Decimal | Net Asset Value | nav_history.csv |


## 03_aum_by_fund_house.csv

| Column Name | Data Type | Business Definition | Source |
|-------------|------------|---------------------|---------|
| fund_house | Text | Name of the Asset Management Company | aum_by_fund_house.csv |
| month | Date | Reporting month for AUM data | aum_by_fund_house.csv |
| aum_cr | Decimal | Assets Under Management in crores | aum_by_fund_house.csv |

## 04_monthly_sip_inflows.csv

| Column Name | Data Type | Business Definition | Source |
|-------------|------------|---------------------|---------|
| month | Date | Reporting month for SIP inflows | monthly_sip_inflows.csv |
| sip_inflows_cr | Decimal | SIP inflows in crores | monthly_sip_inflows.csv |

## 05_category_inflows.csv

| Column Name | Data Type | Business Definition | Source |
|-------------|------------|---------------------|---------|
| category | Text | Mutual fund category | category_inflows.csv |
| month | Date | Reporting month | category_inflows.csv |
| inflow_cr | Decimal | Net inflow amount in crores | category_inflows.csv |

## 06_industry_folio_count.csv

| Column Name | Data Type | Business Definition | Source |
|-------------|------------|---------------------|---------|
| month | Date | Reporting month | industry_folio_count.csv |
| category | Text | Mutual fund category | industry_folio_count.csv |
| folio_count | Integer | Number of investor folios | industry_folio_count.csv |

## 07_scheme_performance.csv

| Column Name | Data Type | Business Definition | Source |
|-------------|------------|---------------------|---------|
| amfi_code | Integer | Unique scheme identifier | scheme_performance.csv |
| scheme_name | Text | Name of the mutual fund scheme | scheme_performance.csv |
| return_1yr | Decimal | One-year annualized return (%) | scheme_performance.csv |
| return_3yr | Decimal | Three-year annualized return (%) | scheme_performance.csv |
| return_5yr | Decimal | Five-year annualized return (%) | scheme_performance.csv |
| expense_ratio | Decimal | Annual fund expense ratio (%) | scheme_performance.csv |

## 08_investor_transactions.csv

| Column Name | Data Type | Business Definition | Source |
|-------------|------------|---------------------|---------|
| investor_id | Text | Unique investor identifier | investor_transactions.csv |
| transaction_date | Date | Date of transaction | investor_transactions.csv |
| amfi_code | Integer | Scheme identifier | investor_transactions.csv |
| transaction_type | Text | Type of transaction (SIP/Lumpsum/Redemption) | investor_transactions.csv |
| amount_inr | Decimal | Transaction amount in INR | investor_transactions.csv |
| state | Text | Investor state | investor_transactions.csv |
| city | Text | Investor city | investor_transactions.csv |
| city_tier | Text | Classification of city (T30/B30) | investor_transactions.csv |
| age_group | Text | Investor age group | investor_transactions.csv |
| gender | Text | Investor gender | investor_transactions.csv |
| annual_income_lakhs | Decimal | Annual income in lakhs | investor_transactions.csv |
| payment_mode | Text | Payment method used | investor_transactions.csv |
| kyc_status | Text | Investor KYC verification status | investor_transactions.csv |

## 09_portfolio_holdings.csv

| Column Name | Data Type | Business Definition | Source |
|-------------|------------|---------------------|---------|
| amfi_code | Integer | Scheme identifier | portfolio_holdings.csv |
| company_name | Text | Name of the underlying company | portfolio_holdings.csv |
| sector | Text | Industry sector of the holding | portfolio_holdings.csv |
| market_cap | Text | Market capitalization category | portfolio_holdings.csv |
| holding_percentage | Decimal | Percentage allocation in the portfolio | portfolio_holdings.csv |

## 10_benchmark_indices.csv

| Column Name | Data Type | Business Definition | Source |
|-------------|------------|---------------------|---------|
| index_name | Text | Name of benchmark index | benchmark_indices.csv |
| date | Date | Index reporting date | benchmark_indices.csv |
| index_value | Decimal | Benchmark index value | benchmark_indices.csv |
| daily_return | Decimal | Daily percentage return of the index | benchmark_indices.csv |