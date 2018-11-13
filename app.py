from models import *

# importing dash info
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

all_years = db.session.query(DOC_Annual_Data).all()
all_years_dicts = [fy_ave.to_dict() for fy_ave in all_years]
    
def get_doc_vals(sought_val):
    x_values = []
    y_values = []
    for year in all_years_dicts:
        # print(year)
        if year[sought_val] != None:
            x_values.append(year['fiscal year'])
            y_values.append(int(re.sub("[^0-9]","",year[sought_val])))
    return (list(reversed(x_values)), list(reversed(y_values)))

app.layout = html.Div(
    children = [
        dcc.Graph(
            id="graph1",
            figure={
                'data':[
                    {'x': get_doc_vals('ave inmate pop')[0], 'y': get_doc_vals('ave inmate pop')[1]},
                    {'x': get_doc_vals('inmate admissions')[0], 'y': get_doc_vals('inmate admissions')[1]}
                ]
            }
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)