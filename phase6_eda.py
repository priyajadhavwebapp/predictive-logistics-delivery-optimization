import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# PHASE 6: EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

# Load cleaned dataset
DATA_PATH = "02_Data/processed/cleaned_logistics_data.csv"

data = pd.read_csv(DATA_PATH, encoding="latin1")

print("\n===== PHASE 6: EDA =====")
print("Rows:", data.shape[0])
print("Columns:", data.shape[1])

# Create folder for charts
os.makedirs("05_Visualizations", exist_ok=True)

# ==========================================
# 1. SHIPPING MODE ANALYSIS
# ==========================================

if "Shipping Mode" in data.columns:

    print("\n===== SHIPPING MODE =====")
    print(data["Shipping Mode"].value_counts())

    plt.figure(figsize=(8, 5))
    data["Shipping Mode"].value_counts().plot(kind="bar")
    plt.title("Shipment Count by Shipping Mode")
    plt.xlabel("Shipping Mode")
    plt.ylabel("Number of Shipments")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        "05_Visualizations/shipping_mode_distribution.png"
    )

    plt.show()

# ==========================================
# 2. DELIVERY PERFORMANCE
# ==========================================

if "Delivery Performance" in data.columns:

    print("\n===== DELIVERY PERFORMANCE =====")
    print(data["Delivery Performance"].value_counts())

    plt.figure(figsize=(7, 5))
    data["Delivery Performance"].value_counts().plot(kind="bar")

    plt.title("Delivery Performance")
    plt.xlabel("Performance")
    plt.ylabel("Number of Shipments")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig(
        "05_Visualizations/delivery_performance.png"
    )

    plt.show()

# ==========================================
# 3. DELIVERY DELAY ANALYSIS
# ==========================================

if "Delivery Delay" in data.columns:

    print("\n===== DELIVERY DELAY =====")

    print(
        data["Delivery Delay"].describe()
    )

    plt.figure(figsize=(8, 5))

    data["Delivery Delay"].hist(
        bins=20
    )

    plt.title("Distribution of Delivery Delays")
    plt.xlabel("Delivery Delay (Days)")
    plt.ylabel("Number of Shipments")
    plt.tight_layout()

    plt.savefig(
        "05_Visualizations/delivery_delay_distribution.png"
    )

    plt.show()

# ==========================================
# 4. ORDER REGION ANALYSIS
# ==========================================

if "Order Region" in data.columns:

    print("\n===== TOP ORDER REGIONS =====")

    region_counts = (
        data["Order Region"]
        .value_counts()
        .head(10)
    )

    print(region_counts)

    plt.figure(figsize=(10, 6))

    region_counts.plot(kind="bar")

    plt.title("Top 10 Order Regions")
    plt.xlabel("Region")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        "05_Visualizations/top_order_regions.png"
    )

    plt.show()

# ==========================================
# 5. SHIPPING TIME ANALYSIS
# ==========================================

if "Days for shipping (real)" in data.columns:

    print("\n===== SHIPPING TIME =====")

    print(
        data["Days for shipping (real)"].describe()
    )

    plt.figure(figsize=(8, 5))

    data["Days for shipping (real)"].value_counts().sort_index().plot(
        kind="bar"
    )

    plt.title("Actual Shipping Days")
    plt.xlabel("Shipping Days")
    plt.ylabel("Number of Shipments")
    plt.tight_layout()

    plt.savefig(
        "05_Visualizations/actual_shipping_days.png"
    )

    plt.show()

# ==========================================
# 6. BASIC NUMERICAL RELATIONSHIPS
# ==========================================

numeric_columns = [
    "Days for shipping (real)",
    "Days for shipment (scheduled)",
    "Order Item Quantity",
    "Order Item Total",
    "Order Item Product Price"
]

existing_columns = [
    column
    for column in numeric_columns
    if column in data.columns
]

print("\n===== NUMERICAL CORRELATION =====")

if existing_columns:
    print(
        data[existing_columns].corr()
    )

# ==========================================
# FINAL MESSAGE
# ==========================================

print("\n===== PHASE 6 COMPLETED =====")
print("EDA analysis completed successfully.")
print("Charts saved in:")
print("05_Visualizations/")