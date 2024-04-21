# Libraries
import streamlit as st
from PIL import Image


# Confit
st.set_page_config(page_title='MacroPlanner Tool', page_icon='Home Icon', layout='wide')

my_global_routing_dataframe = None

#engine = sqlalchemy.create_engine(CONNECTION)

# Title
st.title('Macro Planner Upgrade Tool')

# Blockchains
c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.image(Image.open('images/arbitrum-logo.png'))
c2.image(Image.open('images/avalanche-logo.png'))
c3.image(Image.open('images/bsc-logo.png'))
c4.image(Image.open('images/ethereum-logo.png'))
c5.image(Image.open('images/optimism-logo.png'))
c6.image(Image.open('images/polygon-logo.png'))

# TOol Overview
st.write(
    """
    This tool is used to generate all files that are used to run the monthly S&OP process.  Refer to specific documentation if you need more information.  Click on the navigation on the left hand side to go to the specific file that needs to be updated
    """
)

# Methodology
st.subheader('Methodology')
st.write(
    """
    This tool is built with Streamlit that is a Python based tool with a UI frontend
    """
)

# Divider
st.divider()
