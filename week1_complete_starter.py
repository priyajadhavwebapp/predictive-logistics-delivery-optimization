import pandas as pd
import numpy as np

# Location of the logistics dataset
DATA_PATH = "02_Data/raw/logistics_data.csv"

# Load dataset
data = pd.read_csv(DATA_PATH, encoding="latin1")

print("\n===== DATASET LOADED SUCCESSFULLY =====")
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])

print("\n===== FIRST 5 ROWS =====")
print(data.head())

print("\n===== COLUMN NAMES =====")
print(data.columns.tolist())

print("\n===== DATA TYPES =====")
print(data.dtypes)

print("\n===== MISSING VALUES =====")
print(data.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print("Duplicates:", data.duplicated().sum())

print("\n===== NUMERICAL SUMMARY =====")
print(data.describe())

print("\n===== PHASE 4 COMPLETED =====")