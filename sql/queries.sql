-- Query 1: Top 5 Funds by AUM

SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Query 2: Average NAV per Fund

SELECT amfi_code,
AVG(nav) AS avg_nav
FROM nav_history
GROUP BY amfi_code;

-- Query 3: Monthly Average NAV

SELECT strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- Query 4: Transactions by State

SELECT state,
COUNT(*) AS total_transactions,
SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- Query 5: Funds with Expense Ratio < 1%

SELECT scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- Query 6: Average Return by Category

SELECT category,
AVG(return_3yr_pct) AS avg_return_3yr
FROM scheme_performance
GROUP BY category;

-- Query 7: Top 10 Investors by Investment Amount

SELECT investor_id,
SUM(amount_inr) AS total_investment
FROM investor_transactions
GROUP BY investor_id
ORDER BY total_investment DESC
LIMIT 10;

-- Query 8: Transaction Type Distribution

SELECT transaction_type,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY transaction_type;

-- Query 9: Highest Sharpe Ratio Funds

SELECT scheme_name,
sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- Query 10: Fund House Wise Scheme Count

SELECT fund_house,
COUNT(*) AS scheme_count
FROM fund_master
GROUP BY fund_house
ORDER BY scheme_count DESC;
