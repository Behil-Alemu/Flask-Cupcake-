"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcake_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True



connect_db(app)
db.create_all()

def serialize_dessert(cupcake):
    """Serialize a cupcakes SQLAlchemy obj to dictionary."""
    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image}
@app.route("/")
def homepage():
    """Homepage with cupcake form and cupcake list"""
    cupcakes = Cupcake.query.all()
    return render_template("index.html", cupcakes=cupcakes)



@app.route("/api/cupcakes")
def list_cupcakes():
    """list all the cupcakes JSON form"""
    cupcakes = Cupcake.query.all()
    serialized=[serialize_dessert(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route("/api/cupcakes/<cupcake_id>")
def list_single_cupcake(cupcake_id):
    """list a single cupcake in  JSON form"""

    cupcake = Cupcake.query.get(cupcake_id)
    serialized = serialize_dessert(cupcake)
    

    return jsonify(cupcake=serialized)

@app.route("/api/cupcakes", methods=["POST"])
def add_cupcakes():
    """Creates a new cupcake and returns JSON of that new cupcake"""
    print(request.json)
    # flavor = request.json["flavor"]
    # size= request.json["size"]
    # rating= request.json["rating"]
    # image= request.json["image"]
    new_cup= Cupcake(flavor=request.json["flavor"],size=request.json["size"],rating=request.json["rating"], image=request.json["image"])
    # new_cup= Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cup)
    db.session.commit()

    serialized = serialize_dessert(new_cup)

    return (jsonify(cupcake=serialized), 201)


@app.route('/api/cupcakes/<cupcake_id>', methods=["PATCH"])
def update_cupcakes(cupcake_id):
    """Updates a particular cupcake from the list"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    serialized = serialize_dessert(cupcake)
    db.session.commit()
    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes/<cupcake_id>', methods=["DELETE"])
def delete_todo(cupcake_id):
    """Deletes a particular todo"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")



