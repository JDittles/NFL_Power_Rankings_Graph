import plotly 
plotly.tools.set_credentials_file(username='CodeBros', api_key='hpNSBNmapnnHGKhDIQig')
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from ESPN_Scraper import *

build_espn_rankings()

def graph_power_rankings():
    data = []
    for each in TeamSymbol:
        data.append(go.Scatter(
            x = range(1, 18),
            y = ESPN_LstDict.get(each),
            mode = each,
            name = each,
            line = dict(
                color = 'rgb' + str(Team_Color_Primary.get(each)),
                width = '5')))
    layout = dict(title = 'NFL Power Rankings',
              xaxis = dict(title = 'Week'),
              yaxis = dict(title = 'Ranking 1-32'),
              )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig)

