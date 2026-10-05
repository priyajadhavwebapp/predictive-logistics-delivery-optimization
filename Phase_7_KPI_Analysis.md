# Phase 7 – KPI Analysis and Visualization

## KPI Calculations

```python
total_shipments = len(data)

on_time_shipments = len(
    data[data["Delivery Status"] == "On Time"]
)

on_time_rate = (on_time_shipments / total_shipments) * 100

print("On-Time Delivery Rate:", on_time_rate)

# Example:
# average_delivery_time = data["Delivery Time"].mean()
# print("Average Delivery Time:", average_delivery_time)
```

## Recommended Visualizations
1. Delivery Status Distribution
2. Average Delivery Time by Shipping Mode
3. Delays by Region
4. Shipment Volume Over Time
5. Transportation Cost by Shipping Mode

## Deliverable
A KPI summary table plus 3–5 charts.
