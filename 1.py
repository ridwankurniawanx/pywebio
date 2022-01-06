#from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import info as session_info
from pywebio.output import put_html
import plotly.graph_objects as go
import pandas as pd
import pywebio

pywebio.config(theme="dark")
# Read data from a csv
def a():
    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

    fig = go.Figure(data=[go.Surface(z=z_data.values) ])

    fig.update_layout(template="plotly_dark",title='Mt Bruno Elevation', autosize=True,
                    width=720, height=720,
                    margin=dict(l=65, r=50, b=65, t=90))

    html = fig.to_html(include_plotlyjs="require", full_html=False )
    put_html(html)

pywebio.start_server(a,port=8080)

