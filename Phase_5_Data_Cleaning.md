# Phase 5 – Data Cleaning and Preprocessing

## Tasks
- Handle missing values appropriately.
- Remove duplicate records if justified.
- Convert date columns to datetime.
- Check numerical columns for invalid values.
- Standardize categorical values where necessary.
- Create useful derived variables such as delivery time or delay.

## Starter Code
```python
import pandas as pd

data = pd.read_csv("../02_Data/raw/logistics_data.csv")

print(data.isnull().sum())
print("Duplicates:", data.duplicated().sum())

data = data.drop_duplicates()

# Example date conversion:
# data["Order Date"] = pd.to_datetime(data["Order Date"])
# data["Delivery Date"] = pd.to_datetime(data["Delivery Date"])

# Example feature:
# data["Delivery Time"] = (
#     data["Delivery Date"] - data["Order Date"]
# ).dt.days
```

## Important
Do not fabricate missing information. Document the reason for every important cleaning decision.
