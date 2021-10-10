
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from app import app

# df = px.data.gapminder()
df = pd.read_csv("data/Fifa_new_ranks.csv")


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

layout = html.Div([
        html.H3("Team ranks over time: Select the countries you want to compare", style={'text-align': 'center'}),

    dcc.Dropdown(id='dpdn2', value=['Kenya', 'Uganda'], multi=True,
                 options=[{'label': x, 'value': x} for x in
                          df['country_full'].unique()]),
                        dcc.Graph(id="line-chart"),
      
      
])

@app.callback(
    Output("line-chart", "figure"), 
    [Input("dpdn2", "value")])


def update_line_chart(country_chosen):
    mask = df.country_full.isin(country_chosen)
    print(mask)
    
    fig = px.line(df[mask],
              x="Year",
              y="rank",  
              color="country_full")
    #fig.update_xaxes(type='category')
    return fig