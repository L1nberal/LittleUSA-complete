from sqlite3 import dbapi2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app= Flask(__name__)

#  the secret_key is needed in order to maintain sessions in Flask. 
app.secret_key = 'super secret key'

login = LoginManager()
#login is just a variable

#initialize database
db= SQLAlchemy(app)
#db is just a variable

#linking Flask file with database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///linh.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Also, we need to link our SQLAlchemy DB instance (present in models.py file) with the main app. For that, add:
login.init_app(app)
# After that, we tell Flask_login about the page; the unauthenticated 
# users will get redirected
login.login_view= 'login'

#create the database file
db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()

from LittleUSA import routes