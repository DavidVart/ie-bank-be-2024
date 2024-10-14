from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from sqlalchemy import text


import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'

db = SQLAlchemy(app)

# Select environment based on the ENV environment variable
if os.getenv('ENV') == 'local':
    print("Running in local mode")
    app.config.from_object('config.LocalConfig')
elif os.getenv('ENV') == 'dev':
    print("Running in development mode")
    app.config.from_object('config.DevelopmentConfig')
elif os.getenv('ENV') == 'ghci':
    print("Running in github mode")
    app.config.from_object('config.GithubCIConfig')


from iebank_api.models import Account

with app.app_context():
    # # Uncomment to add the country column to the account table
    # query = text("ALTER TABLE account ADD COLUMN country VARCHAR(32)")
    # db.session.execute(query)
    # db.session.commit()

    db.create_all()
CORS(app)

from iebank_api import routes