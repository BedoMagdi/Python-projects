import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import database as db
import calendar
from datetime import datetime


## Settings
incomes = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expeneses", "Savings"]
curreny = "USD"
page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:" # for emojis
layout = "centered"


st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)


## Drop down 
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])

## db
def get_all_periods():
    items = db.fetch_all_periods()
    periods = [item["key"] for item in items]
    return periods


##  Hide some style
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)


## Navigation
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],
    orientation="horizontal"
)

## Input
if selected == "Data Entry":
    st.header("Data Entry in {}".format(curreny))
    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1.selectbox("Select Month", months, key="month")
        col1.selectbox("Select Year", years, key="year")

        "---"
        with st.expander("Income"):
            for income in incomes:
                st.number_input(f"{income}", key=income, min_value=0, format="%i", step=10)

        with st.expander("Expense"):
            for expense in expenses:
                st.number_input(f"{expense}", key=expense, min_value=0, format="%i", step=10)

        with st.expander("Comment"):
            comment = st.text_area("", placeholder="Add Comment", key="comment")

        "---"
        submitted = st.form_submit_button("Save Data")
        if submitted:
            period = str(st.session_state.year) + "_" + str(st.session_state.month)
            incomes = {income: st.session_state[income] for income in incomes}
            except_ = {expense: st.session_state[expense] for expense in expenses}
            db.insert_period(period, incomes, except_, comment)
            st.success("Data saved!")


## Plot
if selected == "Data Visualization":
    st.header("Data Visualization")
    with st.form("saved_periods"):
        period = st.selectbox("Select Period", get_all_periods())
        submitted = st.form_submit_button("Plot Period")
        if submitted:
            period_data = db.get_period(period)
            comment = period_data.get("comment")
            expenses = period_data.get("expenses")
            incomes = period_data.get("incomes")

            # Some metrics
            total_income = sum(incomes.values())
            total_expense = sum(expenses.values())
            remaining_income = total_income - total_expense
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Income", f"{total_income} { curreny}")
            col2.metric("Total Expense", f"{total_expense} { curreny}")
            col3.metric("Remaining Income", f"{remaining_income} { curreny}")
            st.text(f"Comment: {comment}")

            # Create sankey chart
            label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
            source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
            target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
            value = list(incomes.values()) + list(expenses.values())

            # Data to dict, dict to sankey
            link = dict(source=source, target=target, value=value)
            node = dict(label=label, pad=20, thickness=30, color="#E694FF")
            data = go.Sankey(link=link, node=node)

            # Plot it!
            fig = go.Figure(data)
            fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
            st.plotly_chart(fig, use_container_width=True)