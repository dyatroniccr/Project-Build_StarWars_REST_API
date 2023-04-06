from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),  unique=False, nullable=False)
    height = db.Column(db.String(20), unique=False, nullable=False)
    mass = db.Column(db.String(20), unique=False, nullable=False)    
    hair_color = db.Column(db.String(20), unique=False, nullable=False)
    skin_color = db.Column(db.String(20), unique=False, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=False)
    eye_color = db.Column(db.String(20), unique=False, nullable=False)
    birth_year = db.Column(db.String(30), unique=False, nullable=False)
    homeworld = db.Column(db.String(250), unique=False, nullable=False)
    url = db.Column(db.String(250), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,        
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "gender": self.gender,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "homeworld": self.homeworld,
            "url": self.url
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    diameter = db.Column(db.String(50), unique=False, nullable=False)
    rotation_period = db.Column(db.String(50), unique=False, nullable=False)
    orbital_period = db.Column(db.String(50), unique=False, nullable=False)
    gravity = db.Column(db.String(50), unique=False, nullable=False)
    population = db.Column(db.String(100), unique=False, nullable=False)
    climate = db.Column(db.String(100), unique=False, nullable=False)
    terrain = db.Column(db.String(100), unique=False, nullable=False)
    surface = db.Column(db.String(250), unique=False, nullable=False)
    url = db.Column(db.String(250), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,        
            "name": self.name,
            "url": self.url
            # do not serialize the password, its a security breach
        }
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    model = db.Column(db.String(100), unique=False, nullable=False)
    starship_class = db.Column(db.String(100), unique=False, nullable=False)
    manufacturer = db.Column(db.String(100), unique=False, nullable=False)
    length = db.Column(db.String(20), unique=False, nullable=False)
    crew = db.Column(db.String(20), unique=False, nullable=False)
    passengers = db.Column(db.String(20), unique=False, nullable=False)
    max_atmosphering_speed = db.Column(db.String(20), unique=False, nullable=False)
    hyperdrive_rating = db.Column(db.String(20), unique=False, nullable=False)
    mglt = db.Column(db.String(20), unique=False, nullable=False)
    capacity = db.Column(db.String(20), unique=False, nullable=False)
    consumables = db.Column(db.String(50), unique=False, nullable=False)
    pilots = db.Column(db.String(250), unique=False, nullable=False)
    url = db.Column(db.String(250), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,        
            "name": self.name,
            "model": self.model,
            "starship_class": self.starship_class,
            "pilots": self.pilots,
            "url": self.url
            # do not serialize the password, its a security breach
        }
