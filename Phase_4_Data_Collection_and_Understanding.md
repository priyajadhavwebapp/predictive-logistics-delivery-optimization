# Phase 4 – Data Collection and Understanding

## Tasks
1. Download the selected public logistics dataset.
2. Place the original file in `02_Data/raw/`.
3. Load it using pandas.
4. Inspect rows, columns, data types and summary statistics.
5. Document missing values and duplicate records.

## Starter Code
```python
import pandas as pd
import numpy as np

data = pd.read_csv("../02_Data/raw/logistics_data.csv")

print(data.head())
print(data.shape)
print(data.columns)
print(data.info())
print(data.describe())
print(data.isnull().sum())
print("Duplicates:", data.duplicated().sum())
```

## Deliverable
Create a short dataset profile containing:
- Dataset size
- Column descriptions
- Data types
- Missing values
- Duplicate count
- Important variables
