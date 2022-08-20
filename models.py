"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG ="https://tinyurl.com/demo-cupcake"


def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Make a model for cupcake"""
    __tablename__ = "cupcake"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True ) 
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMG )
