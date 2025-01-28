from flask import Flask

f
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config[

app = Flask(__name__)
ap


app = Flask(__name__)


app =
'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///popcornhour.db'
app.config[
app.config
'SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login


db = SQLAlchemy(app)
login_manager = LoginManager(app


db = SQLAlchemy(app)
login_manager = Login


db = SQLAlchemy(app)
login


db = SQL


db = 


db
'login'

from routes import setup_routes

setup_routes(app)



if __name__ == '__main__':
    app.run(debug=
    ap

   
True)
