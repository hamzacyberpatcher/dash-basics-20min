# import the relevant packages
from dash import Dash, html, dash_table
import pandas as pd

# init the app
app = Dash()

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# app layouy
app.layout = [html.Div(children='Hello World'),
              dash_table.DataTable(data=df.to_dict('records'), page_size=10)
              ]

# start running the app
if __name__ == '__main__':
    app.run(debug=True)