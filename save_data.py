

import csv

machines = [
    {
        "machine_name": "CNC 162",
        "part_name": "Bevel Box",
        "target_production": 88,
        "actual_production": 72
    },
    {
        "machine_name": "CNC 28",
        "part_name": "Shaft",
        "target_production": 100,
        "actual_production": 90
    }
]

with open("production_data.csv", "w", newline="") as file:
    columns = [
        "machine_name",
        "part_name",
        "target_production",
        "actual_production"
    ]

    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(machines)

print("Production data saved successfully!")
