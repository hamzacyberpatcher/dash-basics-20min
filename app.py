# import the relevant packages
from dash import Dash, html

# init the app
app = Dash()

# app layouy
app.layout = [html.Div(children='Hello World')]

# start running the app
if __name__ == '__main__':
    app.run(debug=True)