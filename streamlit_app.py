#import google_auth_httplib2
#import httplib2'''
import pandas as pd
import streamlit as st
from gsheetsdb import connect
#'''from google.oauth2 import service_account
#from googleapiclient.discovery import build
#from googleapiclient.http import HttpRequest

#SCOPE = "https://www.googleapis.com/auth/spreadsheets"
#SPREADSHEET_ID = "1QlPTiVvfRM82snGN6LELpNkOwVI1_Mp9J9xeJe-QoaA"
#SHEET_NAME = "Database"'''

GSHEET_URL = f"https://docs.google.com/spreadsheets/d/1NDKV6vm6R8-8DYeSAbUfQuzgv_4b6jWz8PpL0C3qNxU/edit#gid=0"
conn = connect()
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")
st.set_page_config(page_title="Sistema de recomendação de filme", page_icon="🐞", layout="centered")

st.title("🐞 Sistema de recomendação de filme")

st.sidebar.write(
    f"Dataset[Google Sheet]({GSHEET_URL})"
)

form = st.form(key="annotation")

with form:
    cols = st.columns((1, 1))
    author = cols[0].text_input("Report author:")
    bug_type = cols[1].selectbox(
        "Bug type:", ["Front-end", "Back-end", "Data related", "404"], index=2
    )
    comment = st.text_area("Comment:")
    cols = st.columns(2)
    date = cols[0].date_input("Bug date occurrence:")
    bug_severity = cols[1].slider("Bug severity:", 1, 5, 2)
    submitted = st.form_submit_button(label="Submit")

if submitted:
    add_row_to_gsheet(
        gsheet_connector,
        [[author, bug_type, comment, str(date), bug_severity]],
    )
    st.success("Thanks! Your bug was recorded.")
    st.balloons()

expander = st.expander("See all records")
with expander:
    st.write(f"Open original [Google Sheet]({GSHEET_URL})")
    st.dataframe(get_data(gsheet_connector))
