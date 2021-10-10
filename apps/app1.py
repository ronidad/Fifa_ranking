import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px 
import pandas as pd

from app import app

df = pd.read_csv("data/Fifa_new_ranks.csv")
# df['Total_deaths'] = df['Death_Illicit_drugs']+df['Death_Opioid']+df['Death_Alchohol']+df['Death_Other_drugs']+df['Death_Amphetamine']
# df = df[['Entity','Year','Total_deaths']]


layout = html.Div([

    html.H2("African teams ranks each year", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     
                     {"label": "1995", "value": 1995},
                     {"label": "2000", "value": 2000},
                     {"label": "2005", "value": 2005},
                     {"label": "2010", "value": 2010},
                     {"label": "2015", "value": 2015},
                     {"label": "2017", "value": 2017}],
                 multi=False,
                 value=2015,
                 style={'width': "60%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    # print(option_slctd)
    print(type(option_slctd))

    container = "Team rank in: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    #dff = dff[dff["Entity"] == "Entity"]
    print(dff[dff["Year"] == 2015])

    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='country names',
        locations='country_full',
        scope="africa",
        color='rank',
        hover_data=['country_full', 'rank'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'country_full'},
        template='gridon'
    )

   

    return container, fig