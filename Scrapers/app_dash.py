import plotly 
plotly.tools.set_credentials_file(username='CodeBros', api_key='hpNSBNmapnnHGKhDIQig')
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from ESPN_Scraper import *
import csv

def write_espn_rankings_csv():
    build_espn_rankings()
    with open('dash_values.csv', 'w') as csvfile:
        fieldnames = ['TeamSymbol','ESPN_Ranking']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for each in TeamSymbol:
            rank = ESPN_LstDict.get(each)
            writer.writerow({'TeamSymbol': each, 'ESPN_Ranking':rank})
        df = csv.DictReader('dash_values.csv')

write_espn_rankings_csv()

df = pd.read_csv('dash_values.csv')

app = dash.Dash()


app.layout = html.Div([
#    html.Label('Team Choice'),
#    dcc.Dropdown(
#        options=[
#            {'label': 'Philadelphia Eagles', 'value': 25},
#           {'label': 'Dallas Cowboys', 'value': 8},
#        ],
#        value=25
#    ),
    dcc.Graph(
        id='NFL Power Rankings',
        figure={
            'data': [
                go.Scatter(
                    x=range(1, 18),
                    y=df['ESPN_Ranking'[i]]['ESPN_Ranking'],
                    text=df[df[i]]['TeamSymbol'],
                ) for i in df
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
])

if __name__ == '__main__':
    app.run_server()
