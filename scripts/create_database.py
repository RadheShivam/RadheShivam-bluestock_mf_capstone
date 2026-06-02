import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# Database path
db_path = "data/db/bluestock_mf.db"

# Create SQLite connection
engine = create_engine(f"sqlite:///{db_path}")

processed_path = Path("data/processed")

# Load cleaned files into database
for file in processed_path.glob("*.csv"):

    table_name = file.stem.replace("_cleaned", "")

    df = pd.read_csv(file)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table_name} : {len(df)} rows")

print("\nDatabase Created Successfully!")