from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

'''
flask db init to initialize the database
flask db migrate to migrate new changes
flask db upgrade to upgrade and so on.
'migrations' directory will be auto created after run the above commands
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner', lazy="dynamic")

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    # new = db.Column(db.String(20)) # remove this column and upgrade using migrate
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))

if __name__ == "__main__":
    app.run()