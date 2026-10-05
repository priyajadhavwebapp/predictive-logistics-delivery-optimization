import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ==========================================
# PHASE 8: DATA SCIENCE METHODOLOGIES
# ==========================================

DATA_PATH = "02_Data/processed/cleaned_logistics_data.csv"

data = pd.read_csv(DATA_PATH, encoding="latin1")

print("\n===== PHASE 8: DATA SCIENCE METHODOLOGIES =====")

os.makedirs("04_Analysis", exist_ok=True)

# ==========================================
# PART 1: REGRESSION
# Predict actual shipping time
# ==========================================

target = "Days for shipping (real)"

features = [
    "Days for shipment (scheduled)",
    "Order Item Quantity",
    "Order Item Product Price"
]

# Keep only columns that exist
available_features = [
    column for column in features
    if column in data.columns
]

print("\nRegression features:")
print(available_features)

if target in data.columns and len(available_features) >= 1:

    regression_data = data[
        available_features + [target]
    ].copy()

    regression_data = regression_data.dropna()

    X = regression_data[available_features]
    y = regression_data[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    print("\n===== REGRESSION RESULTS =====")

    print("Mean Absolute Error:",
          round(mae, 3))

    print("R2 Score:",
          round(r2, 3))

else:

    print("\nRegression could not be performed.")
    print("Required columns were not found.")


# ==========================================
# PART 2: CLUSTERING
# Group similar shipments
# ==========================================

cluster_features = [
    "Days for shipping (real)",
    "Days for shipment (scheduled)",
    "Order Item Quantity",
    "Order Item Product Price"
]

available_cluster_features = [
    column
    for column in cluster_features
    if column in data.columns
]

print("\nClustering features:")
print(available_cluster_features)

if len(available_cluster_features) >= 2:

    cluster_data = data[
        available_cluster_features
    ].copy()

    cluster_data = cluster_data.dropna()

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(
        cluster_data
    )

    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    clusters = kmeans.fit_predict(
        scaled_data
    )

    cluster_data["Shipment_Cluster"] = clusters

    print("\n===== CLUSTERING RESULTS =====")

    print(
        cluster_data["Shipment_Cluster"]
        .value_counts()
        .sort_index()
    )

    cluster_data.to_csv(
        "04_Analysis/shipment_clusters.csv",
        index=False
    )

    print(
        "\nCluster results saved to:"
    )

    print(
        "04_Analysis/shipment_clusters.csv"
    )

else:

    print("\nClustering could not be performed.")


# ==========================================
# PART 3: OPTIMIZATION STRATEGY
# ==========================================

print("\n===== OPTIMIZATION STRATEGY =====")

print("""
The following optimization strategies are proposed:

1. Assign shipments to suitable transportation modes.

2. Prioritize delayed or high-risk shipments.

3. Allocate logistics resources based on shipment volume.

4. Group similar shipments to improve transportation planning.

5. Reduce unnecessary transportation time and cost.

6. Monitor delivery KPIs regularly.

7. Use predicted delivery time to support shipment planning.
""")


# ==========================================
# FINAL
# ==========================================

print("\n===== PHASE 8 COMPLETED =====")

print("Regression analysis completed.")

print("Clustering analysis completed.")

print("Optimization strategy documented.")

print("\nPhase 8 outputs saved in:")
print("04_Analysis/")