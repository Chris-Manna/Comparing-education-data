from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

import re

# initialize new flask app
app = Flask(__name__)

# add configurations and database URI
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# conect SQLAlchemy to the configured flask app
db = SQLAlchemy(app)

# create models for application
class DOC_Annual_Data(db.Model):
    __tablename__= 'doc_annual_data'
    id = db.Column(db.Integer, primary_key=True)
    fiscal_year = db.Column(db.Text, nullable=False)
    average_inmate_population = db.Column(db.Integer)
    # inmate_admissions = db.Column(db.Text)
    def to_dict(self):
        fy_ave = {
            'id': self.id, 
            'fiscal year': self.fiscal_year, 
            'ave inmate pop': self.average_inmate_population
            # 'inmate admissions': self.inmate_admissions
        }
        return fy_ave
        
