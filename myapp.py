import streamlit as st
import pandas as pd

dat = pd.read_csv("Salaries.csv")
dat.rename(columns = {"yrs.since.phd" : "phd", 
            "yrs.service" : "service"}, inplace = True)

st.title("Salaries in US universities")
selected = st.selectbox("Choose a variable", ["salary", "service", "phd"])

selected_table = dat[selected].describe()
st.table(selected_table)