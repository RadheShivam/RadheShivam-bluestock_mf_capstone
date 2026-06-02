'''
import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print(data.keys())

nav_df = pd.DataFrame(data["data"])

print(nav_df.head())

nav_df.to_csv(
    "data/raw/hdfc_top100_live_nav.csv",
    index=False
)

print("NAV data saved successfully!")

'''

import requests
import pandas as pd
from pathlib import Path

output_folder = Path("data/raw")

funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, amfi_code in funds.items():

    try:
        url = f"https://api.mfapi.in/mf/{amfi_code}"

        response = requests.get(url)

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = output_folder / f"{fund_name}.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"✅ Saved: {fund_name}")

    except Exception as e:
        print(f"❌ Error in {fund_name}")
        print(e)

print("\nAll NAV files downloaded successfully!")