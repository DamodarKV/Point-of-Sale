import streamlit as st
import pandas as pd

from services.sales_service import get_sales_kpis
from services.item_service import get_item_performance
from utils.kpi import get_kpis


def show_analytics():
    st.title("📊 Cafe Analytics Dashboard")

    # -------------------------------
    # KPIs (Top Row)
    # -------------------------------
    revenue, orders, avg_bill = get_kpis()

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Revenue", f"₹{revenue:,.2f}")
    col2.metric("🧾 Orders", orders)
    col3.metric("📈 Avg Bill", f"₹{avg_bill:,.2f}")

    st.divider()

    # ===============================
    # MAIN ROW → Sales + Items
    # ===============================
    col_left, col_right = st.columns(2)

    # -------------------------------
    # SALES KPIs
    # -------------------------------
    with col_left:
        st.subheader("📊 Sales Overview")

        sales = get_sales_kpis()

        c1, c2 = st.columns(2)
        c3, c4 = st.columns(2)

        c1.metric("Yearly Sales", f"₹{sales['yearly']:,.0f}")
        c2.metric("Monthly Sales", f"₹{sales['monthly']:,.0f}")
        c3.metric("Weekly Sales", f"₹{sales['weekly']:,.0f}")
        c4.metric("Today's Sales", f"₹{sales['today']:,.0f}")

    # -------------------------------
    # TOP ITEMS TABLE
    # -------------------------------
    with col_right:
        st.subheader("🍔 Top 5 Items")

        df_items = get_item_performance()

        if not df_items.empty:
            top5 = df_items.head(5).copy()

            # Add ranking
            top5.insert(0, "Rank", range(1, 6))

            # Rename columns
            top5.columns = ["Rank", "Item", "Quantity Sold", "Revenue"]

            # Format revenue
            top5["Revenue"] = top5["Revenue"].apply(lambda x: f"₹{x:,.0f}")

            st.dataframe(top5, use_container_width=True, hide_index=True)
        else:
            st.warning("No item data")