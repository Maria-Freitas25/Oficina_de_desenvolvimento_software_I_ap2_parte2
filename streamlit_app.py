import google_auth_httplib2
import httplib2
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
@st.experimental_singleton()
def connect_to_gsheet():
    # Create a connection object.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["public_gsheets_url"],
    )

# Create a new Http() object for every request
    def build_request(http, *args, **kwargs):
        new_http = google_auth_httplib2.AuthorizedHttp(
            credentials, http=httplib2.Http()
        )
        return HttpRequest(new_http, *args, **kwargs)

    authorized_http = google_auth_httplib2.AuthorizedHttp(
        credentials, http=httplib2.Http()
    )
    service = build(
        "sheets",
        "v4",
        requestBuilder=build_request,
        http=authorized_http,
    )
    gsheet_connector = service.spreadsheets()
    return gsheet_connector


def get_data(gsheet_connector) -> pd.DataFrame:
    values = (
        gsheet_connector.values()
        .execute()
    )

    df = pd.DataFrame(values["values"])
    df.columns = df.iloc[0]
    df = df[1:]
    return df


def add_row_to_gsheet(gsheet_connector, row) -> None:
    gsheet_connector.values().append(

        body=dict(values=row),
        valueInputOption="USER_ENTERED",
    ).execute()

st.title(":lady_beetle: Sistema de recomendação de filme")

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
