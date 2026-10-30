
import os
from dotenv import load_dotenv

load_dotenv()
import pandas as pd
import mysql.connector



df = pd.read_csv("production_data.csv")

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS production_data (
    production_id INT PRIMARY KEY,
    production_date DATE,
    machine_name VARCHAR(50),
    part_name VARCHAR(50),
    target_production INT,
    actual_production INT,
    defect_quantity INT,
    downtime_minutes INT
)
"""

cursor.execute(create_table_query)

insert_query = """
INSERT INTO production_data (
    production_id,
    production_date,
    machine_name,
    part_name,
    target_production,
    actual_production,
    defect_quantity,
    downtime_minutes
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
production_date = VALUES(production_date),
machine_name = VALUES(machine_name),
part_name = VALUES(part_name),
target_production = VALUES(target_production),
actual_production = VALUES(actual_production),
defect_quantity = VALUES(defect_quantity),
downtime_minutes = VALUES(downtime_minutes)
"""

data = []

for _, row in df.iterrows():
    data.append((
        int(row["production_id"]),
        str(row["production_date"]),
        row["machine_name"],
        row["part_name"],
        int(row["target_production"]),
        int(row["actual_production"]),
        int(row["defect_quantity"]),
        int(row["downtime_minutes"])
    ))

cursor.executemany(insert_query, data)
connection.commit()

print("Dataset loaded successfully!")
print("Total records processed:", len(data))

cursor.close()
connection.close()
