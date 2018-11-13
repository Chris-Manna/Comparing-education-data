import dash
import dash_core_components as dcc
import dash_html_components as html

# Flask(__name__)
app = dash.Dash(__name__)


app.layout = html.Div(
    children = [
        html.H2('whattup'), html.H2('world'),dcc.Graph(
            id = 'example-graph',
            figure={
                'data':[
                    {'x': [1,2,3], 'y':[4,5,6], 'type': 'bar', 'name': 'SF'}
                ]
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)