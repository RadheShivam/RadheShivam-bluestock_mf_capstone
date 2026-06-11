# 📊 Mutual Fund Analytics and Investor Intelligence System

## Bluestock Capstone Project

### Project Overview

This project presents an end-to-end **Mutual Fund Analytics and Investor Intelligence System** developed as part of the Bluestock Capstone Program. The objective of this project is to analyze mutual fund performance, investor behavior, SIP trends, portfolio concentration, and market insights using advanced analytics and business intelligence techniques.

The project integrates **Python, SQLite, Jupyter Notebook, Power BI, and GitHub** to build a comprehensive analytics platform capable of generating actionable investment insights.

---

## Objectives

* Analyze mutual fund performance using risk and return metrics.
* Study investor behavior through transaction analytics.
* Evaluate SIP trends and market movements.
* Develop advanced financial risk analytics.
* Create interactive Power BI dashboards.
* Generate investment recommendations based on risk appetite.
* Demonstrate end-to-end data analytics workflow from ETL to reporting.

---

## Datasets Used

The project utilizes ten datasets related to mutual funds and investor transactions:

1. `01_fund_master.csv`
2. `02_nav_history.csv`
3. `03_aum_by_fund_house.csv`
4. `04_monthly_sip_inflows.csv`
5. `05_category_inflows.csv`
6. `06_industry_folio_count.csv`
7. `07_scheme_performance.csv`
8. `08_investor_transactions.csv`
9. `09_portfolio_holdings.csv`
10. `10_benchmark_indices.csv`

---

## Project Architecture

```text
Raw Datasets (CSV Files)
        │
        ▼
Python ETL Pipeline
        │
        ▼
Data Cleaning & Transformation
        │
        ▼
SQLite Database & Processed CSVs
        │
        ▼
Advanced Analytics (Jupyter Notebook)
        │
        ▼
Power BI Dashboards
        │
        ▼
Business Insights & Recommendations
```

---

## Folder Structure

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_performance_analysis.ipynb
│   ├── 03_investor_analytics.ipynb
│   ├── 04_dashboard_preparation.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── explore_fund_master.py
│   ├── validate_amfi_codes.py
│   ├── recommender.py
│   └── run_pipeline.py
│
├── sql/
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   └── Dashboard.pdf
│
├── reports/
│   ├── Final_Report.pdf
│   ├── var_cvar_report.csv
│   ├── rolling_sharpe_chart.png
│   └── charts/
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Requests
* Matplotlib
* Plotly
* SQLite
* SQLAlchemy
* Jupyter Notebook
* Power BI
* Git & GitHub

---

## ETL Pipeline

The ETL process involved:

### Extract

* Importing multiple CSV datasets.
* Fetching live NAV data using APIs.

### Transform

* Handling missing values.
* Removing duplicate records.
* Converting date formats.
* Standardizing data types.
* Feature engineering for analytics.

### Load

* Storing cleaned datasets in SQLite.
* Exporting processed files for Power BI.

---

## Advanced Analytics Implemented

### Historical VaR and CVaR

Calculated downside risk using the 95% confidence level.

### Rolling 90-Day Sharpe Ratio

Measured risk-adjusted returns over time.

### Investor Cohort Analysis

Grouped investors by their first investment year to analyze behavior.

### SIP Continuity Analysis

Identified investors at risk of discontinuing SIP contributions.

### Fund Recommendation System

Recommended top-performing funds based on Sharpe Ratio and investor risk appetite.

### Sector HHI Concentration Analysis

Measured portfolio diversification using the Herfindahl-Hirschman Index (HHI).

---

## Power BI Dashboard

The dashboard consists of four interactive pages:

### Page 1: Industry Overview

* KPI Cards
* Industry AUM Trend
* AUM by AMC

### Page 2: Fund Performance

* Return vs Risk Analysis
* Fund Scorecard
* NAV vs Benchmark Performance

### Page 3: Investor Analytics

* Transaction Amount by State
* SIP / Lumpsum / Redemption Split
* Age Group Analysis
* Monthly Transaction Volume

### Page 4: SIP & Market Trends

* SIP Inflow vs Nifty Trend
* Category-wise Market Share
* Category Inflow Trends
* Top Categories by Net Inflow

---

## Key Insights

* Industry AUM exhibited consistent growth over the analysis period.
* Liquid funds attracted the highest net inflows.
* Most investors were identified as at-risk based on SIP continuity analysis.
* Diversified funds dominated the equity universe according to HHI analysis.
* Risk-adjusted performance varied significantly across mutual fund categories.

---

## How to Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

### Execute Master Pipeline

```bash
python scripts/run_pipeline.py
```

### Fetch Live NAV Data

```bash
python scripts/live_nav_fetch.py
```

### Launch Power BI Dashboard

Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

---

## Deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* bluestock_mf_dashboard.pbix
* Dashboard.pdf
* var_cvar_report.csv
* rolling_sharpe_chart.png
* recommender.py
* Advanced_Analytics.ipynb

---

## Author

**Shivam Kumar Mehta**

Bachelor of Technology (B.Tech)
Lovely Professional University

---

## License

This project was developed for educational and portfolio purposes as part of the Bluestock Capstone Program.
