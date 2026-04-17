import streamlit as st

def show_navbar():
    st.sidebar.title("☕ Cafe POS")

    menu = st.sidebar.radio(
        "Navigation",
        ["Analytics","Menu", "Billing", "Reports", "Inventory","Purchase",],
        index=0
    )

    st.sidebar.markdown("---")
    st.sidebar.caption("© 2026 Cafe System")

    return menu