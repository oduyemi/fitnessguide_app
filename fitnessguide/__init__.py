from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__,instance_relative_config=True)
#csrf = CSRFProtect(app)

#load the config
app.config.from_pyfile('config.py', silent=False)

db = SQLAlchemy(app)
#load the routes 
from fitnessguide import adminroute,userroute  