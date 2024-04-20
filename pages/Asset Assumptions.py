# Libraries
import altair as alt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Asset Assumptions', page_icon=':bar_chart:', layout='wide')

uploaded_files = st.file_uploader("Upload a CSV file", type=["csv"],accept_multiple_files=True)

st.header("Planned DT")

# Check if a file was uploaded
if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        # Read each uploaded CSV file
        df_csv = pd.read_csv(uploaded_file)
        new_header = df_csv.iloc[6] #grab the 6th row for the header
        df_csv = df_csv[7:] #take the data less the header row
        df_csv.columns = new_header #set the header row as the df header
        df_append = pd.concat([df_csv], ignore_index=True)
        
st.write("Uploaded DataFrame:",  df_append)

metric = st.sidebar.multiselect('Select Metric',df_append.Date)
filtered_df = df_append[df_append['Date'].isin(metric)]


#st.line_chart(filtered_df)
