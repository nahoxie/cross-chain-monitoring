# Libraries
import altair as alt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import pandas as pd

data_planned_dt ={"Asset":["OSW-HM","OSW-HM"],
                  "Month":["April 2024","May 2024"],
                  "Hours":[72,24]}
st.set_page_config(page_title='Routing', page_icon=':bar_chart:', layout='wide')

df_data_planned_dt=pd.DataFrame(data_planned_dt)

st.header("Planned DT")
#st.data_editor(df_data_planned_dt,num_rows="dynamic")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the DataFrame
    st.write("Uploaded DataFrame:",  df.iloc[7:])



st.asset = st.sidebar.multiselect('Select Month',["April","May"])
