from models import db, DOC_Annual_Data
import requests

# creates the DOC_Annual_Data model and table in the database
db.create_all()

def make_api_request(url = "https://data.cityofnewyork.us/resource/ns8x-c6af.json"):
    request_content = requests.get(url)
    outcomes = request_content.json()
    return outcomes

def get_doc_data(url = "https://data.cityofnewyork.us/resource/hh4y-wm6k.json"):
    doc_stats = make_api_request(url)
    for stat in doc_stats:
        if stat["statistic_type_name"] == 'Average Daily Inmate Population':
            # get each row in the data base
            fy_data = DOC_Annual_Data(fiscal_year=stat['fiscal_year'], average_inmate_population=stat["statistic_type_count"])
            db.session.add(fy_data)
        if stat["statistic_type_name"] == 'Annual Inmate Admissions':
            fy_data = DOC_Annual_Data(fiscal_year=stat['fiscal_year'], inmate_admissions=stat["statistic_type_count"])
            db.session.add(fy_data)

def get_comp_data(url = 'https://data.cityofnewyork.us/resource/9s4h-37hy.json'):
    comp_stats = make_api_request(url)
    # return len(comp_stats)
    all_complaints = {}
    unique_years = []
    
    for stat in comp_stats:
        comp_year = stat["cmplnt_fr_dt"][0:4]
        if comp_year not in unique_years:
            unique_years.append(comp_year)
        
        # # if comp_year 
        # if stat["law_cat_cd"] in all_complaints.keys():
        #     stat["law_cat_cd"]]  += 1
        # else:
        #     all_complaints[stat["law_cat_cd"]] = 1
    return unique_years
print(get_comp_data())

# get_doc_data()
# db.session.commit()