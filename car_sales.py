
# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('pakwheels_used_car_data_v02.csv')

# Initialize the app - incorporate css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div([
    html.Div(className='row', children='Used Cars Sales Analysis',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),

    html.Div(className='row', children=[
        dcc.RadioItems(options=[
                            {'label': 'Mileage', 'value': 'mileage'},
                            {'label': 'Price', 'value': 'price'},
                            # Add more options based on available columns in your dataset
                       ],
                       value='mileage',
                       inline=True,
                       id='my-radio-buttons')
    ]),

    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dash_table.DataTable(data=df.to_dict('records'), page_size=11, style_table={'overflowX': 'auto'})
        ]),
        html.Div(className='six columns', children=[
            dcc.Graph(figure={}, id='graph')
        ])
    ])
])

# Add controls to build the interaction
@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='my-radio-buttons', component_property='value')
)
def update_graph(selected_column):
    fig = px.histogram(df, x='make', y=selected_column, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

