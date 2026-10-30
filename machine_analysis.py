
import os
from dotenv import load_dotenv
import pandas as pd
import mysql.connector

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
query = """
SELECT
    machine_name,
    SUM(target_production) AS total_target,
    SUM(actual_production) AS total_production,
    SUM(target_production - actual_production) AS production_loss,
    SUM(defect_quantity) AS total_defects,
    SUM(downtime_minutes) AS total_downtime
FROM production_data
GROUP BY machine_name
"""

df = pd.read_sql(query, connection)
connection.close()

df["efficiency_percentage"] = (
    df["total_production"] / df["total_target"] * 100
).round(2)

df["defect_rate_percentage"] = (
    df["total_defects"] / df["total_production"] * 100
).round(2)

df = df.sort_values(
    by="efficiency_percentage",
    ascending=False
)

print("\nMachine Performance Report")
print(df.to_string(index=False))



import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.bar(
    df["machine_name"],
    df["efficiency_percentage"]
)

plt.title("Machine-wise Production Efficiency")
plt.xlabel("Machine Name")
plt.ylabel("Efficiency (%)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


