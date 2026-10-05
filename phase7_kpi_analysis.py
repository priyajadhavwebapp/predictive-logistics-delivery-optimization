import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# PHASE 7: KPI ANALYSIS & VISUALIZATION
# ==========================================

DATA_PATH = "02_Data/processed/cleaned_logistics_data.csv"

data = pd.read_csv(DATA_PATH, encoding="latin1")

print("\n===== PHASE 7: KPI ANALYSIS =====")

os.makedirs("05_Visualizations", exist_ok=True)

# ==========================================
# 1. TOTAL SHIPMENTS
# ==========================================

total_shipments = len(data)

print("\nTotal Shipments:", total_shipments)

# ==========================================
# 2. AVERAGE SHIPPING TIME
# ==========================================

if "Days for shipping (real)" in data.columns:

    average_shipping_time = data["Days for shipping (real)"].mean()

    print(
        "Average Shipping Time:",
        round(average_shipping_time, 2),
        "days"
    )

# ==========================================
# 3. AVERAGE SCHEDULED SHIPPING TIME
# ==========================================

if "Days for shipment (scheduled)" in data.columns:

    average_scheduled_time = (
        data["Days for shipment (scheduled)"].mean()
    )

    print(
        "Average Scheduled Shipping Time:",
        round(average_scheduled_time, 2),
        "days"
    )

# ==========================================
# 4. SHIPPING DELAY
# ==========================================

if (
    "Days for shipping (real)" in data.columns
    and "Days for shipment (scheduled)" in data.columns
):

    data["Delay_Days"] = (
        data["Days for shipping (real)"]
        - data["Days for shipment (scheduled)"]
    )

    average_delay = data["Delay_Days"].mean()

    delayed_shipments = (
        data["Delay_Days"] > 0
    ).sum()

    delay_rate = (
        delayed_shipments / total_shipments
    ) * 100

    print(
        "Average Delay:",
        round(average_delay, 2),
        "days"
    )

    print(
        "Delayed Shipments:",
        delayed_shipments
    )

    print(
        "Delay Rate:",
        round(delay_rate, 2),
        "%"
    )

# ==========================================
# 5. ORDER FULFILLMENT / DELIVERY STATUS
# ==========================================

if "Delivery Status" in data.columns:

    print("\n===== DELIVERY STATUS =====")

    status_counts = data["Delivery Status"].value_counts()

    print(status_counts)

    plt.figure(figsize=(9, 5))

    status_counts.plot(kind="bar")

    plt.title("Delivery Status Distribution")
    plt.xlabel("Delivery Status")
    plt.ylabel("Number of Shipments")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        "05_Visualizations/delivery_status_kpi.png"
    )

    plt.show()

# ==========================================
# 6. SHIPPING MODE KPI
# ==========================================

if (
    "Shipping Mode" in data.columns
    and "Days for shipping (real)" in data.columns
):

    mode_analysis = (
        data.groupby("Shipping Mode")
        ["Days for shipping (real)"]
        .mean()
        .sort_values()
    )

    print("\n===== AVERAGE SHIPPING TIME BY MODE =====")
    print(mode_analysis)

    plt.figure(figsize=(9, 5))

    mode_analysis.plot(kind="bar")

    plt.title("Average Shipping Time by Shipping Mode")
    plt.xlabel("Shipping Mode")
    plt.ylabel("Average Shipping Days")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        "05_Visualizations/average_shipping_time_by_mode.png"
    )

    plt.show()

# ==========================================
# 7. ORDER REGION ANALYSIS
# ==========================================

if "Order Region" in data.columns:

    region_counts = (
        data["Order Region"]
        .value_counts()
        .head(10)
    )

    print("\n===== TOP 10 ORDER REGIONS =====")
    print(region_counts)

    plt.figure(figsize=(10, 6))

    region_counts.plot(kind="bar")

    plt.title("Top 10 Order Regions")
    plt.xlabel("Region")
    plt.ylabel("Number of Shipments")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        "05_Visualizations/top_10_regions_kpi.png"
    )

    plt.show()

# ==========================================
# FINAL
# ==========================================

print("\n===== PHASE 7 COMPLETED =====")
print("KPI analysis completed successfully.")
print("Visualizations saved in:")
print("05_Visualizations/")