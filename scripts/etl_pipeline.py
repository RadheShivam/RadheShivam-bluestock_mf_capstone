from pathlib import Path
import pandas as pd

data_path = Path("data/raw")

csv_files = list(data_path.glob("*.csv"))

print(f"Total CSV files found: {len(csv_files)}")

for file in csv_files:

    print("\n" + "="*60)
    print(f"FILE: {file.name}")
    print("="*60)

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")