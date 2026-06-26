# import pandas as pd
# from pathlib import Path
# from sqlalchemy import create_engine

# # Database path
# db_path = "data/db/bluestock_mf.db"

# # Create SQLite connection
# engine = create_engine(f"sqlite:///{db_path}")

# processed_path = Path("data/processed")

# # Load cleaned files into database
# for file in processed_path.glob("*.csv"):

#     table_name = file.stem.replace("_cleaned", "")

#     df = pd.read_csv(file)

#     df.to_sql(
#         table_name,
#         engine,
#         if_exists="replace",
#         index=False
#     )

#     print(f"Loaded {table_name} : {len(df)} rows")

# print("\nDatabase Created Successfully!")





import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# ==========================
# Database Configuration
# ==========================

db_path = "data/db/bluestock_mf.db"

# Create SQLite connection
engine = create_engine(f"sqlite:///{db_path}")

processed_path = Path("data/processed")

# ==========================
# Load all cleaned CSVs
# ==========================

for file in processed_path.glob("*.csv"):

    # Table name = filename without "_cleaned"
    table_name = (
    file.stem
    .replace("_cleaned", "")
    .replace("01_", "")
    .replace("02_", "")
    .replace("03_", "")
    .replace("04_", "")
    .replace("05_", "")
    .replace("06_", "")
    .replace("07_", "")
    .replace("08_", "")
    .replace("09_", "")
    .replace("10_", "")
)

    # Read cleaned CSV
    df = pd.read_csv(file)

    # Load into SQLite
    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    # Verify row count
    db_count = pd.read_sql(
        f"SELECT COUNT(*) AS cnt FROM {table_name}",
        engine
    ).iloc[0]["cnt"]

    if len(df) == db_count:
        print(f"✅ {table_name}: {db_count} rows verified")
    else:
        print(
            f"❌ {table_name}: CSV={len(df)}, DB={db_count}"
        )

print("\n===================================")
print("Database Created Successfully!")
print("All tables loaded and verified.")
print("===================================")