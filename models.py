"""Models for Cupcake app."""
from email.mime import image
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

    # def serialize(self):
    #     """Returns a dict representation of todo which we can turn into JSON"""
    #     return {
    #         'id': self.id,
    #         'flavor': self.flavor,
    #         'size': self.size,
    #         'rating': self.rating,
    #         'image': self.image
    #     }
    #     response_json = jsonify(cupcake=new_cup.serialize())
    #     return (response_json, 201)