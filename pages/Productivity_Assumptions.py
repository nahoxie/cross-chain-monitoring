# Libraries
import altair as alt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import pandas as pd

#Tabs    
tab1, tab2 = st.tabs(["Tons Per Hour", "Recovery"])

with tab1:
  st.header("Tons Per Hour")

with tab2:
  st.header("Recovery")
