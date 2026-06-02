import pandas as pd

# Load fund master data
df = pd.read_csv("data/raw/01_fund_master.csv")

print("\n========== UNIQUE FUND HOUSES ==========")
print(df["fund_house"].unique())

print("\n========== UNIQUE CATEGORIES ==========")
print(df["category"].unique())

print("\n========== UNIQUE SUB-CATEGORIES ==========")
print(df["sub_category"].unique())

print("\n========== UNIQUE RISK CATEGORIES ==========")
print(df["risk_category"].unique())

print("\n========== COUNTS ==========")
print(f"Fund Houses: {df['fund_house'].nunique()}")
print(f"Categories: {df['category'].nunique()}")
print(f"Sub-Categories: {df['sub_category'].nunique()}")
print(f"Risk Categories: {df['risk_category'].nunique()}")