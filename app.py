from models import *

# importing dash info
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

all_years = db.session.query(DOC_Annual_Data).all()
all_years_dicts = [fy_ave.to_dict() for fy_ave in all_years]

def get_ave_inmate_values():
    x_values = []
    y_values = []
    for year in all_years_dicts:
        # print(year)
        if year["ave inmate pop"] != None:
            x_values.append(year['fiscal year'])
            y_values.append(int(re.sub("[^0-9]","",year['ave inmate pop'])))
    return (x_values, y_values)
    
def get_admissions_values():
    x_values = []
    y_values = []
    for year in all_years_dicts:
        # print(year)
        if year["inmate admissions"] != None:
            x_values.append(year['fiscal year'])
            y_values.append(int(re.sub("[^0-9]","",year['inmate admissions'])))
    return (x_values, y_values)


# print(get_x_values())
app.layout = html.Div(
    children = [
        dcc.Graph(
            id="graph1",
            figure={
                'data':[
                    {'x': get_ave_inmate_values()[0], 'y': get_ave_inmate_values()[1]},
                    {'x': get_admissions_values()[0], 'y': get_admissions_values()[1]}
                ]
            }
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)