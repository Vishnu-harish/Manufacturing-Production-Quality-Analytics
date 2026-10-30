
import pandas as pd
import random
from datetime import date, timedelta

random.seed(42)

machines = ["CNC 162", "CNC 28", "CNC 45", "CNC 60", "CNC 75"]
parts = ["Bevel Box", "Shaft", "Gear", "Housing", "Bracket"]

records = []
start_date = date(2026, 1, 1)

for i in range(1000):
    target = random.randint(80, 120)
    actual = random.randint(60, target)
    defects = random.randint(0, min(10, actual))
    downtime = random.randint(0, 90)

    records.append({
        "production_id": i + 1,
        "production_date": start_date + timedelta(days=i % 90),
        "machine_name": random.choice(machines),
        "part_name": random.choice(parts),
        "target_production": target,
        "actual_production": actual,
        "defect_quantity": defects,
        "downtime_minutes": downtime
    })

df = pd.DataFrame(records)
df.to_csv("production_data.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(df))
print(df.head())
