
import csv

with open("production_data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for machine in reader:
        target = int(machine["target_production"])
        actual = int(machine["actual_production"])

        loss = target - actual
        efficiency = (actual / target) * 100

        print("Machine:", machine["machine_name"])
        print("Production Loss:", loss)
        print("Efficiency:", round(efficiency, 2), "%")
        print("-" * 30)
