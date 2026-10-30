
import pandas as pd

df = pd.read_csv("production_data.csv")

df["production_loss"] = (
    df["target_production"] - df["actual_production"]
)

df["efficiency_percentage"] = (
    df["actual_production"] / df["target_production"] * 100
).round(2)

print("Complete Production Analysis:")
print(df)

print("\nMachine-wise Efficiency:")
print(df[["machine_name", "efficiency_percentage"]])

print("\nTotal Production Loss:")
print(df["production_loss"].sum())

print("\nAverage Efficiency:")
print(round(df["efficiency_percentage"].mean(), 2), "%")


print("\n--- Data Quality Check ---")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

