# Libraries
import altair as alt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import pandas as pd
from PIL import Image

# Config
st.set_page_config(page_title='Routing', page_icon=':bar_chart:', layout='wide')
start_date = datetime.now().replace(day=1).date()
date_range = {'Month':[start_date + relativedelta(months=i) for i in range(18)]}

#Tabs    
tab1, tab2, tab3 = st.tabs(["Automotive", "Can","Specialties"])

with tab1:
  table_data = [[]]
	for _ in range(2):
        table_data[0].append(None)

    # Create a Streamlit UI for the table
  st.title("Table with Buttons")

  # Create a table
  table = st.table(table_data)

# Add buttons to each cell
	for i in range(1):
   	 	for j in range(2):
        	button_label = f"Button {i}-{j}"
        	if table_data[i][j] is None:
            	table_data[i][j] = st.button(button_label)

# Display the table
table.table(table_data) 
  st.header("Automotive Demand for the next 18 months")
  uploaded_files = st.file_uploader("Upload a CSV file for demand", type=["csv"],accept_multiple_files=false)
  st.button("Save Auto demand")
# Generate a sequence of dates for the next 18 months
# Create a DataFrame with the dates
  df_demand_Auto = pd.DataFrame(date_range, columns=['Month'])
  df_demand_pivot_Auto = df_demand_Auto.transpose()
  df_demand_pivot_Auto.columns = df_demand_pivot_Auto.iloc[0]
  df_demand_pivot_Auto = df_demand_pivot_Auto[1:]
  edited_demand_data_Auto= st.data_editor(df_demand_pivot_Auto,num_rows="dynamic",height=1001)
  chart_demand_data_Auto = edited_demand_data_Auto.transpose().apply(pd.to_numeric, errors='coerce')
  st.dataframe(edited_demand_data_Auto)
  st.bar_chart(chart_demand_data_Auto)
  
with tab2:
  st.header("Can Demand for the next 18 months")
  st.button("Save Can demand")
#  st.text(datetime.now().replace(day=1).date())
# Generate a sequence of dates for the next 18 months
# Create a DataFrame with the dates
  df_demand_Can = pd.DataFrame(date_range, columns=['Month'])
  df_demand_pivot_Can = df_demand_Can.transpose()
  df_demand_pivot_Can.columns = df_demand_pivot_Can.iloc[0]
  df_demand_pivot_Can = df_demand_pivot_Can[1:]
  edited_demand_data_Can= st.data_editor(df_demand_pivot_Can,num_rows="dynamic",height=1000)
  chart_demand_data_Can = edited_demand_data_Can.transpose().apply(pd.to_numeric, errors='coerce')
  st.dataframe(edited_demand_data_Can)
  st.bar_chart(chart_demand_data_Can)

with tab3:
  st.header("Specialties Demand for the next 18 months")
  st.button("Save Specialties demand")
# st.text(datetime.now().replace(day=1).date())
# Generate a sequence of dates for the next 18 months
# Create a DataFrame with the dates
  df_demand_Specialties = pd.DataFrame(date_range, columns=['Month'])
  df_demand_pivot_Specialties = df_demand_Specialties.transpose()
  df_demand_pivot_Specialties.columns = df_demand_pivot_Specialties.iloc[0]
  df_demand_pivot_Specialties = df_demand_pivot_Specialties[1:]
  edited_demand_data_Specialties= st.data_editor(df_demand_pivot_Auto,num_rows="dynamic",height=1002)
  chart_demand_data_Specialties = edited_demand_data_Specialties.transpose().apply(pd.to_numeric, errors='coerce')
  st.dataframe(edited_demand_data_Specialties)
  st.bar_chart(chart_demand_data_Specialties)



first_filter = st.sidebar.multiselect('Select DPP',chart_demand_data_Auto.columns)


#st.dataframe(chart_demand_data_Auto[chart_demand_data['index'].str.contains(first_filter, case=False)])
st.session_state["df_demand_pivot"] = df_demand_pivot_Auto
