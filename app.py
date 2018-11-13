from models import *

# importing dash info
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

all_years = db.session.query(DOC_Annual_Data).all()
all_years_dicts = [fy_ave.to_dict() for fy_ave in all_years]

def get_x_values():
    x_values = []
    y_values = []
    for year in all_years_dicts:
        x_values.append(year['fiscal year'])
        y_values.append(int(re.sub("[^0-9]","",year['ave inmate pop'])))
    return (x_values, y_values)

app.layout = html.Div(
    children = [
        dcc.Graph(
            id="graph1",
            figure={
                'data':[
                    {'x': get_x_values()[0], 'y':get_x_values()[1] }
                ]
            }
        )
    ]
)

# @app.route('/education')
# def education_data():
#     return render_template("show.html")

if __name__ == '__main__':
    app.run_server(debug=True)