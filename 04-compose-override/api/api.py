from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgrespassword@postgres_db:5432/postgres'
db = SQLAlchemy(app)


class RequestLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)


db.drop_all()    
db.create_all()


@app.route('/')
def hello_world():
    # Log the request.
    request = RequestLog(timestamp=datetime.utcnow())
    db.session.add(request)
    db.session.commit()
    
    return f'Hello, Docker! Your request ID is {request.id}\n'
