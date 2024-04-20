# Libraries
import altair as alt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import pandas as pd
from mitosheet.streamlit.v1 import spreadsheet

data_planned_dt ={"Asset":["OSW-HM","OSW-HM"],
                  "Month":["April 2024","May 2024"],
                  "Hours":[72,24]}

df_data_planned_dt=pd.DataFrame(data_planned_dt)



st.header("Planned DT")
#st.data_editor(df_data_planned_dt,num_rows="dynamic")
st.spreadsheet(df_data_planned_dt)
st.asset = st.sidebar.multiselect('Select Month',["April","May"])
