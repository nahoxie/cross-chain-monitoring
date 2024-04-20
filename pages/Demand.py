# Libraries
import altair as alt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import pandas as pd

# Config
st.set_page_config(page_title='Routing', page_icon=':bar_chart:', layout='wide')

#Tabs    
tab1, tab2 = st.tabs(["Annual Demand", "Monthly Demand"])

with tab1:
  st.header("Annual Demand")
  
with tab2:
  st.header("Monthly Demand")
# Generate a sequence of dates for the next 18 months
date_range = [start_date + relativedelta(months=i) for i in range(18)]

# Create a DataFrame with the dates
df_demand = pd.DataFrame(date_range, columns=['Date'])
df_demand_pivot = df_demand.transpose()
df_demand_pivot.columns = df_demand_pivot.iloc[0]
df_demand_pivot = df_demand_pivot[1:]