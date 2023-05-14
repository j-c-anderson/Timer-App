import pandas as pd
import streamlit as st
from gsheetsdb import connect

# Read data from Google Sheet. URL saved in Secrets with Streamlit
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def data_load(sheet_url):
    csv_url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = data_load(st.secrets["gsheet_url"])

st.write(df)

st.write('hello world')
