# Libraries
import altair as alt
import numpy as np
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import pandas as pd\
import io
import zipfile

zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
    for file_name, data in csv.items():
        zip_file.writestr(file_name, data.encode("utf-8"))

# Display a download button for the zip file
st.download_button(
    label="Download All DataFrames as Zip",
    data=zip_buffer,
    file_name="my_dataframes.zip",
    mime="application/zip",
)
