import streamlit as st

from components.navbar import show_navbar
from pages.analytics import show_analytics
from pages.billing import show_billing
from pages.reports import show_reports
from pages.inventory import show_inventory
from pages.menu import show_menu
from pages.purchase import show_purchase

st.set_page_config(page_title="Cafe POS", layout="wide")

# -------------------------------
# NAVIGATION
# -------------------------------
menu = show_navbar()

# -------------------------------
# ROUTING
# -------------------------------
if menu == "Analytics":
    show_analytics()

elif menu == "Billing":
    show_billing()

elif menu == "Reports":
    show_reports()

elif menu == "Inventory":
    show_inventory()

elif menu == "Menu":
    show_menu()

elif menu == "Purchase":
    show_purchase()