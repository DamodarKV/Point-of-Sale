import pandas as pd
import numpy as np

np.random.seed(42)

# ---------------------------
# SALES DATA
# ---------------------------
def generate_sales_kpis():
    yearly = np.random.randint(1500000, 3000000)
    monthly = np.random.randint(100000, 300000)
    weekly = np.random.randint(20000, 80000)
    today = np.random.randint(2000, 10000)

    return {
        "yearly": yearly,
        "monthly": monthly,
        "weekly": weekly,
        "today": today
    }
def generate_sales_data():
    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)

    data = {
        "day": dates,
        "revenue": np.random.randint(2000, 10000, size=len(dates))
    }

    return pd.DataFrame(data)


# ---------------------------
# ITEM PERFORMANCE
# ---------------------------
def generate_item_data():
    items = [
        "Espresso", "Cappuccino", "Latte", "Cold Coffee",
        "Sandwich", "Burger", "Pasta", "Tea"
    ]

    df = pd.DataFrame({
        "item_name": items,
        "qty": np.random.randint(20, 200, len(items)),
        "revenue": np.random.randint(5000, 30000, len(items))
    })

    return df.sort_values(by="qty", ascending=False)


# ---------------------------
# INVENTORY
# ---------------------------
def generate_inventory_data():
    items = ["Milk", "Coffee Beans", "Sugar", "Bread", "Cheese"]

    df = pd.DataFrame({
        "item_name": items,
        "stock_quantity": np.random.randint(0, 50, len(items))
    })

    return df


# ---------------------------
# PROFIT DATA
# ---------------------------
def generate_profit_data():
    revenue = np.random.randint(100000, 200000)
    cost = np.random.randint(50000, 120000)

    return pd.DataFrame({
        "revenue": [revenue],
        "cost": [cost],
        "profit": [revenue - cost]
    })


# ---------------------------
# KPIs
# ---------------------------
def generate_kpis():
    revenue = np.random.randint(100000, 200000)
    orders = np.random.randint(200, 500)
    avg_bill = revenue / orders

    return revenue, orders, avg_bill