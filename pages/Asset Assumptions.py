# Libraries
import altair as alt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader("Upload a CSV file", type=["csv"],accept_multiple_files=True)

st.header("Planned DT")

# Check if a file was uploaded
if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        # Read each uploaded CSV file
        df_csv = pd.read_csv(uploaded_file)
        st.write("Uploaded DataFrame:",  df_csv)
#new_header = df_csv.iloc[6] #grab the 6th row for the header
#df_csv = df_csv[7:] #take the data less the header row
#df_csv.columns = new_header #set the header row as the df header

#df = pd.concat([df, df_csv], ignore_index=True)


#metric = st.sidebar.multiselect('Select Metric',df_csv.Date)
#filtered_df = df_csv[df_csv['Date'].isin(metric)]


#st.line_chart(filtered_df)
