# Mutual Fund Analytics Capstone Project

## Project Overview

This project focuses on Mutual Fund Analytics using Python, Pandas, APIs, SQL, and Data Visualization tools.

The objective is to analyze mutual fund performance, NAV history, SIP inflows, AUM trends, portfolio holdings, investor behavior, and benchmark indices.

---

## Datasets Used

1. 01_fund_master.csv
2. 02_nav_history.csv
3. 03_aum_by_fund_house.csv
4. 04_monthly_sip_inflows.csv
5. 05_category_inflows.csv
6. 06_industry_folio_count.csv
7. 07_scheme_performance.csv
8. 08_investor_transactions.csv
9. 09_portfolio_holdings.csv
10. 10_benchmark_indices.csv

---

## Day 1 Tasks Completed

* Project folder structure created
* Git repository initialized
* GitHub repository connected
* Required Python libraries installed
* All CSV datasets loaded successfully
* Data quality checks performed
* Live NAV data fetched from mfapi.in
* NAV data downloaded for 5 mutual fund schemes
* Fund master exploration completed
* AMFI code validation completed

---

## Folder Structure

bluestock_mf_capstone/

* data/

  * raw/
  * processed/
  * db/

* notebooks/

* scripts/

  * etl_pipeline.py
  * live_nav_fetch.py
  * explore_fund_master.py
  * validate_amfi_codes.py

* sql/

* dashboard/

* reports/

* requirements.txt

* README.md

---

## Technologies Used

* Python
* Pandas
* NumPy
* Requests
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* Jupyter Notebook
* Git & GitHub

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Run ETL pipeline:

python scripts/etl_pipeline.py

Fetch live NAV data:

python scripts/live_nav_fetch.py

Explore fund master:

python scripts/explore_fund_master.py

Validate AMFI codes:

python scripts/validate_amfi_codes.py

##
