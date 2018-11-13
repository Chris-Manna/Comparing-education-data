from graduate_outcomes import make_api_request
# from sqlalchemy_flask import DOC_Annual_Data
from models import db, DOC_Annual_Data

# creates the DOC_Annual_Data model and table in the database
db.create_all()

def get_doc_data(url = "https://data.cityofnewyork.us/resource/hh4y-wm6k.json"):
    doc_stats = make_api_request(url)
    for stat in doc_stats:
        if stat["statistic_type_name"] == 'Average Daily Inmate Population':
            # get each row in the data base
            fy_data = DOC_Annual_Data(fiscal_year=stat['fiscal_year'], average_inmate_population=stat["statistic_type_count"])
            db.session.add(fy_data) 
        # if stat["statistic_type_name"] == 'Annual Inmate Admissions':
        #     fy_data = DOC_Annual_Data(fiscal_year=stat['fiscal_year'], statistic_type_count=stat[statistic_type_count])
        #     db.session.add(fy_data)
get_doc_data()

db.session.commit()