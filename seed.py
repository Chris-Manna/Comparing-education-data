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

get_doc_data()

db.session.commit()
    

    
# daniel = User(username="Daniel")
# jeff = User(username="Jeff")
# rachel = User(username="rachel")
# 
# daniel.tweets = [Tweet(text="I love hogs"), Tweet(text="Hogs are the best way to teach react"), Tweet(text="programming is lyfe")]
# jeff.tweets = [Tweet(text="Data Science is awesome"), Tweet(tweet="Python is pretty neat"), Tweet(text="Wishing I was chillin' in Mexico rn")]
# rachel.tweets = [Tweet(text="RPDR is the best show"), Tweet(text="I just made the coolest NPM package!"), Tweet(text="running is so fun!")]
# 
# db.session.add(jeff)
# db.session.add(rachel)
# db.session.add(daniel)
# db.session.commit()