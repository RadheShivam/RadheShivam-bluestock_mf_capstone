# import pandas as pd
# from pathlib import Path

# raw_path = Path("data/raw")
# processed_path = Path("data/processed")

# processed_path.mkdir(exist_ok=True)

# # ==========================
# # NAV HISTORY CLEANING
# # ==========================

# nav = pd.read_csv(raw_path / "02_nav_history.csv")

# nav["date"] = pd.to_datetime(nav["date"])

# nav = nav.sort_values(
#     ["amfi_code", "date"]
# )

# nav = nav.drop_duplicates()

# nav = nav[nav["nav"] > 0]

# nav["nav"] = nav["nav"].ffill()

# nav.to_csv(
#     processed_path / "02_nav_history_cleaned.csv",
#     index=False
# )

# print("NAV History Cleaned")

# # ==========================
# # INVESTOR TRANSACTIONS
# # ==========================

# txn = pd.read_csv(
#     raw_path / "08_investor_transactions.csv"
# )

# txn["transaction_date"] = pd.to_datetime(
#     txn["transaction_date"]
# )

# txn["transaction_type"] = (
#     txn["transaction_type"]
#     .str.strip()
#     .str.title()
# )

# txn = txn[
#     txn["amount_inr"] > 0
# ]

# valid_kyc = [
#     "Verified",
#     "Pending"
# ]

# txn = txn[
#     txn["kyc_status"].isin(valid_kyc)
# ]

# txn.to_csv(
#     processed_path /
#     "08_investor_transactions_cleaned.csv",
#     index=False
# )

# print("Investor Transactions Cleaned")

# # ==========================
# # SCHEME PERFORMANCE
# # ==========================

# perf = pd.read_csv(
#     raw_path / "07_scheme_performance.csv"
# )

# return_cols = [
#     "return_1yr_pct",
#     "return_3yr_pct",
#     "return_5yr_pct"
# ]

# for col in return_cols:
#     perf[col] = pd.to_numeric(
#         perf[col],
#         errors="coerce"
#     )

# perf = perf[
#     perf["expense_ratio_pct"]
#     .between(0.1, 2.5)
# ]

# perf.to_csv(
#     processed_path /
#     "07_scheme_performance_cleaned.csv",
#     index=False
# )

# print("Scheme Performance Cleaned")

# print("\nCleaning Complete!")




# Clean the remaing files with basic cleaning steps
import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
processed_path = Path("data/processed")

processed_path.mkdir(exist_ok=True)

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:

    df = pd.read_csv(raw_path / file)

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Convert date columns automatically
    for col in df.columns:
        if "date" in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                pass

    output_name = file.replace(".csv", "_cleaned.csv")

    df.to_csv(
        processed_path / output_name,
        index=False
    )

    print(f"Saved: {output_name}")

print("\nAll remaining files cleaned successfully!")