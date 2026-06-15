import pandas as pd
from sqlalchemy import create_engine

# MySQL Configuration
USERNAME = "root"
PASSWORD = "root"
DATABASE = "traffic_violation_db"

# Database Connection
engine = create_engine(
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@localhost/{DATABASE}"
)

# CSV File Path
file_path = "data/processed/cleaned_traffic_violations.csv"

chunksize = 50000
total_rows = 0

print("Starting Import...")

for chunk in pd.read_csv(
        file_path,
        chunksize=chunksize):

    # Convert column names to lowercase with underscores
    chunk.columns = [
        c.lower()
        .replace(" ", "_")
        .replace("-", "_")
        for c in chunk.columns
    ]

    # Rename columns to match MySQL table
    chunk.rename(columns={
        "seqid": "seq_id",
        "subagency": "sub_agency",
        "vehicletype": "vehicle_type"
    }, inplace=True)

    # Import chunk into MySQL
    chunk.to_sql(
        "traffic_violations",
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    total_rows += len(chunk)

    print(f"Imported {total_rows} rows")

print("Import Completed Successfully")