
# print("Manufacturing Analytics Project")
# print("Production Data Analysis Started")

# machine_id = "M101"
# units_produced = 500
# defective_units = 25

# print("Machine ID:", machine_id)
# print("Units Produced:", units_produced)
# print("Defective Units:", defective_units)



# defect_rate = (defective_units / units_produced) * 100

# good_units = units_produced - defective_units

# print("Good Units:", good_units)
# print("Defect Rate:", defect_rate, "%")


# production_data = [
#     {"machine": "M101", "shift": "Day", "produced": 500, "defective": 25},
#     {"machine": "M102", "shift": "Day", "produced": 600, "defective": 18},
#     {"machine": "M103", "shift": "Night", "produced": 450, "defective": 30}
# ]

# for item in production_data:
#     good_units = item["produced"] - item["defective"]
#     defect_rate = (item["defective"] / item["produced"]) * 100

#     print("\nMachine:", item["machine"])
#     print("Shift:", item["shift"])
#     print("Produced:", item["produced"])
#     print("Good Units:", good_units)
#     print("Defect Rate:", round(defect_rate, 2), "%")


# loss production data 

machine=[{ "machine_name" : "cnc 162",
         "part_name":"bewel box",
         "target_production": 88,
         "actual_production": 72},
         {"machine_name" : "cnc 28",
         "part_name":"side cover",
         "target_production": 120,
         "actual_production": 106
         }]
print("Machine Name:",machine[1]["machine_name"])
print("loss_production","=",machine[1]["target_production"] - machine[1]["actual_production"])



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

for machine in machines:
    target = machine["target_production"]
    actual = machine["actual_production"]

    loss = target - actual
    efficiency = (actual / target) * 100

    print("Machine:", machine["machine_name"])
    print("Part:", machine["part_name"])
    print("Target Production:", target)
    print("Actual Production:", actual)
    print("Production Loss:", loss)
    print("Efficiency:", round(efficiency, 2), "%")
    print("-" * 30)

