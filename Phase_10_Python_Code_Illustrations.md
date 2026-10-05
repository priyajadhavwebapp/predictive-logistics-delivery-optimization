# Phase 10 – Python Code Illustrations

## Data Loading
```python
import pandas as pd
import numpy as np

data = pd.read_csv("../02_Data/raw/logistics_data.csv")
print(data.head())
```

## Data Inspection
```python
print(data.shape)
print(data.columns)
print(data.info())
print(data.describe())
print(data.isnull().sum())
```

## Basic KPI
```python
total_shipments = len(data)
on_time = len(data[data["Delivery Status"] == "On Time"])
on_time_rate = (on_time / total_shipments) * 100

print(on_time_rate)
```

## Regression Illustration
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = data[["Distance", "Weight", "Quantity"]]
y = data["Delivery Time"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

## Clustering Illustration
```python
from sklearn.cluster import KMeans

features = data[["Distance", "Weight", "Quantity"]]

kmeans = KMeans(n_clusters=3, random_state=42)
data["Cluster"] = kmeans.fit_predict(features)
```
