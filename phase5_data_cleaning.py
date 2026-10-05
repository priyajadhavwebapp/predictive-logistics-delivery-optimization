import pandas as pd
import numpy as np
import os

# PHASE 5: DATA CLEANING

# Load original dataset
DATA_PATH = "02_Data/raw/logistics_data.csv"

data = pd.read_csv(DATA_PATH, encoding="latin1")

print("\n===== ORIGINAL DATASET =====")
print("Rows:", data.shape[0])
print("Columns:", data.shape[1])

# 1. Check duplicate rows
duplicate_count = data.duplicated().sum()

print("\n===== DUPLICATE CHECK =====")
print("Duplicate rows:", duplicate_count)

if duplicate_count > 0:
    data = data.drop_duplicates()
    print("Duplicates removed.")
else:
    print("No duplicate rows found.")

# 2. Check missing values
print("\n===== MISSING VALUES =====")

missing_values = data.isnull().sum()
print(missing_values[missing_values > 0])

# 3. Remove completely empty columns
empty_columns = data.columns[data.isnull().all()].tolist()

print("\n===== COMPLETELY EMPTY COLUMNS =====")
print(empty_columns)

if len(empty_columns) > 0:
    data = data.drop(columns=empty_columns)
    print("Empty columns removed.")
else:
    print("No completely empty columns found.")

# 4. Convert date columns
date_columns = [
    "order date (DateOrders)",
    "shipping date (DateOrders)"
]

print("\n===== DATE CONVERSION =====")

for column in date_columns:
    if column in data.columns:
        data[column] = pd.to_datetime(
            data[column],
            errors="coerce"
        )
        print(column, "converted to datetime.")

# 5. Convert numerical columns
numeric_columns = [
    "Order Item Quantity",
    "Order Item Total",
    "Order Item Discount Rate",
    "Order Item Product Price",
    "Days for shipping (real)",
    "Days for shipment (scheduled)"
]

print("\n===== NUMERICAL COLUMNS =====")

for column in numeric_columns:
    if column in data.columns:
        data[column] = pd.to_numeric(
            data[column],
            errors="coerce"
        )
        print(column, "converted to numeric.")

# 6. Remove rows missing essential values
essential_columns = [
    "Days for shipping (real)",
    "Days for shipment (scheduled)",
    "Order Item Quantity",
    "Order Item Total"
]

existing_essential = [
    column for column in essential_columns
    if column in data.columns
]

before_rows = len(data)

if existing_essential:
    data = data.dropna(subset=existing_essential)

after_rows = len(data)

print("\n===== ESSENTIAL DATA CHECK =====")
print("Rows before:", before_rows)
print("Rows after:", after_rows)
print("Rows removed:", before_rows - after_rows)

# 7. Create Delivery Delay
if (
    "Days for shipping (real)" in data.columns
    and
    "Days for shipment (scheduled)" in data.columns
):

    data["Delivery Delay"] = (
        data["Days for shipping (real)"]
        - data["Days for shipment (scheduled)"]
    )

    print("\n===== DELIVERY DELAY =====")
    print(data["Delivery Delay"].describe())

# 8. Create Delivery Performance
if "Delivery Delay" in data.columns:

    data["Delivery Performance"] = np.where(
        data["Delivery Delay"] <= 0,
        "On Time",
        "Delayed"
    )

    print("\n===== DELIVERY PERFORMANCE =====")
    print(data["Delivery Performance"].value_counts())

# 9. Save cleaned dataset
OUTPUT_PATH = "02_Data/processed/cleaned_logistics_data.csv"

os.makedirs("02_Data/processed", exist_ok=True)

data.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\n===== CLEANED DATASET SAVED =====")
print("Saved to:", OUTPUT_PATH)

print("Final rows:", data.shape[0])
print("Final columns:", data.shape[1])

print("\n===== PHASE 5 COMPLETED =====")