# Libraries
import altair as alt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import pandas as pd

st.header("Planned DT")
#st.data_editor(df_data_planned_dt,num_rows="dynamic")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the CSV file
    df_csv = pd.read_csv(uploaded_file)
    #df = df.transpose().apply(pd.to_numeric, errors='coerce')
    # Display the DataFrame
new_header = df_csv.iloc[6] #grab the 6th row for the header
df_csv = df_csv[7:] #take the data less the header row
df_csv.columns = new_header #set the header row as the df header

df = pd.concat([df, df_csv], ignore_index=True)


metric = st.sidebar.multiselect('Select Metric',df.Date)
filtered_df = df[df['Date'].isin(metric)]
st.write("Uploaded DataFrame:",  filtered_df)

st.line_chart(filtered_df)
