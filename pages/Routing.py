# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import data
import altair as alt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import pandas as pd
import io
import zipfile

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Config
st.set_page_config(page_title='Routing', page_icon=':bar_chart:', layout='wide')

data_route = {
    "DPP": ["DPP1", "DPP2", "DPP3","DPP4"],
    "Source": ["OSW-HM", "OSW-HM", "OSW-HM","OSW-HM"],
    "Sink": ["OSW-CM72", "OSW-88", "KIN-CM1","LOG-CM4"],
    "Active":[False,True,False,False]}


my_global_routing_dataframe  = pd.DataFrame(data_route)


st.header("Routing")
st.data_editor(my_global_routing_dataframe,num_rows="dynamic")
st.first_filter = st.sidebar.multiselect('Select DPP',["DPP1","DPP2"])
st.second_filter = st.sidebar.multiselect('Select Source',["OSW-HM"])
