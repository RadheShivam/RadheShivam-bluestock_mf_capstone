-- Dimension Table: Fund

CREATE TABLE dim_fund (
amfi_code INTEGER PRIMARY KEY,
scheme_name TEXT,
fund_house TEXT,
category TEXT,
sub_category TEXT,
risk_category TEXT
);

-- Dimension Table: Date

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY AUTOINCREMENT,
date DATE,
year INTEGER,
quarter INTEGER,
month INTEGER,
day INTEGER
);

-- Fact Table: NAV

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER,
date DATE,
nav REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

-- Fact Table: Transactions

CREATE TABLE fact_transactions (
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
investor_id TEXT,
amfi_code INTEGER,
transaction_date DATE,
transaction_type TEXT,
amount_inr REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

-- Fact Table: Performance

CREATE TABLE fact_performance (
performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
sharpe_ratio REAL,
beta REAL,
expense_ratio_pct REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

-- Fact Table: AUM

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
fund_house TEXT,
date DATE,
aum_crore REAL,
num_schemes INTEGER
);
