# import the relevant packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# init the app
app = Dash()

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# app layout
# pagesize will tell the number of pages
app.layout = [html.Div(children='App with data and graph'),
              dash_table.DataTable(data=df.to_dict('records'), page_size=10),
              dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
              ]

# start running the app
if __name__ == '__main__':
    app.run(debug=True)