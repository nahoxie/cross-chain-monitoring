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
start_date = datetime.now().replace(day=1).date()

#st.first_filter = st.sidebar.multiselect('Select DPP',edited_demand_data.Month)

#Tabs    
tab1, tab2 = st.tabs(["Annual Demand", "Monthly Demand"])

with tab1:
  st.header("Annual Demand")
  
with tab2:
  st.text(datetime.now().replace(day=1).date())
# Generate a sequence of dates for the next 18 months

date_range = {'Month':[start_date + relativedelta(months=i) for i in range(18)]}
#date_range.loc[len(date_range.index)] = ['DPP']



# Create a DataFrame with the dates
df_demand = pd.DataFrame(date_range, columns=['Month'])
df_demand_pivot = df_demand.transpose()
df_demand_pivot.columns = df_demand_pivot.iloc[0]
df_demand_pivot = df_demand_pivot[1:]
edited_demand_data= st.data_editor(df_demand_pivot,num_rows="dynamic")
chart_demand_data = edited_demand_data.transpose().apply(pd.to_numeric, errors='coerce')
st.dataframe(chart_demand_data)
st.bar_chart(chart_demand_data)
