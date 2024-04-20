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

data_route = {
    "MPP": ["MPP1", "MPP2", "MPP3","MPP4"],
    "Source": ["OSW-HM", "OSW-HM", "OSW-HM","OSW-HM"],
    "Sink": ["OSW-CM72", "OSW-88", "KIN-CM1","LOG-CM4"],
    "Active":[False,True,False,False]}

my_global_routing_dataframe  = pd.DataFrame(data_route)

# Config
st.set_page_config(page_title='Routing', page_icon=':bar_chart:', layout='wide')

st.header("Routing")
filtered
st.data_editor(my_global_routing_dataframe,num_rows="dynamic")
st.first_filter = st.sidebar.multiselect('Select MPP',data_route.MPP)









st.session_state["my_global_routing_dataframe"] = my_global_routing_dataframe
