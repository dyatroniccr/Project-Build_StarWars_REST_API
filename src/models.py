from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    favorite_people = db.relationship('FavoritePeople', backref = 'user', lazy=True)
    favorite_planet = db.relationship('FavoritePlanet', backref = 'user', lazy=True)
    favorite_vehicle = db.relationship('FavoriteVehicle', backref = 'user', lazy=True)

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
    height = db.Column(db.String(20), unique=False, nullable=False)
    mass = db.Column(db.String(20), unique=False, nullable=False)    
    hair_color = db.Column(db.String(20), unique=False, nullable=False)
    skin_color = db.Column(db.String(20), unique=False, nullable=False)
    eye_color = db.Column(db.String(20), unique=False, nullable=False)
    birth_year = db.Column(db.String(30), unique=False, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=False)     
    name = db.Column(db.String(250),  unique=False, nullable=False)
    homeworld = db.Column(db.String(250), unique=False, nullable=False)
    url = db.Column(db.String(250), unique=False, nullable=False)
    favorite_people = db.relationship('FavoritePeople', backref = 'people', lazy=True)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,            
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,            
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "name": self.name,
            "homeworld": self.homeworld,
            "url": self.url           
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    diameter = db.Column(db.String(50), unique=False, nullable=False)
    rotation_period = db.Column(db.String(50), unique=False, nullable=False)
    orbital_period = db.Column(db.String(50), unique=False, nullable=False)
    gravity = db.Column(db.String(50), unique=False, nullable=False)
    population = db.Column(db.String(100), unique=False, nullable=False)
    climate = db.Column(db.String(100), unique=False, nullable=False)
    terrain = db.Column(db.String(100), unique=False, nullable=False)
    surface_water = db.Column(db.String(50), unique=False, nullable=False)
    name = db.Column(db.String(250), unique=True, nullable=False)
    url = db.Column(db.String(250), unique=False, nullable=False)
    favorite_planet = db.relationship('FavoritePlanet', backref = 'planet', lazy=True)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,           
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "name": self.name,
            "url": self.url
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    model = db.Column(db.String(100), unique=False, nullable=False)
    starship_class = db.Column(db.String(100), unique=False, nullable=False)
    manufacturer = db.Column(db.String(100), unique=False, nullable=False)
    cost_in_credits = db.Column(db.String(100), unique=False, nullable=False)
    length = db.Column(db.String(20), unique=False, nullable=False)
    crew = db.Column(db.String(20), unique=False, nullable=False)
    passengers = db.Column(db.String(20), unique=False, nullable=False)
    max_atmosphering_speed = db.Column(db.String(20), unique=False, nullable=False)
    hyperdrive_rating = db.Column(db.String(20), unique=False, nullable=False)
    mglt = db.Column(db.String(20), unique=False, nullable=False)
    cargo_capacity = db.Column(db.String(20), unique=False, nullable=False)
    consumables = db.Column(db.String(50), unique=False, nullable=False)
    pilots = db.Column(db.String(250), unique=False, nullable=False)
    name = db.Column(db.String(250), unique=True, nullable=False)
    url = db.Column(db.String(250), unique=False, nullable=False)
    favorite_vehicle = db.relationship('FavoriteVehicle', backref = 'vehicle', lazy=True)

    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,                 
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "mglt": self.mglt,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "pilots": self.pilots,
            "name": self.name,
            "url": self.url            
        }


class FavoritePeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "people_name": People.query.get(self.people_id).serialize()["name"],
            "user_name": User.query.get(self.user_id).serialize()["name"],
            "user": User.query.get(self.user_id).serialize(),
            "people": People.query.get(self.people_id).serialize()
        }

class FavoritePlanet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "planet_name": Planet.query.get(self.planet_id).serialize()["name"],
            "user_name": User.query.get(self.user_id).serialize()["name"],
            "user": User.query.get(self.user_id).serialize(),
            "planet": Planet.query.get(self.planet_id).serialize()
        }

class FavoriteVehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id,
            "vehicle_name": Vehicle.query.get(self.vehicle_id).serialize()["name"],
            "user_name": User.query.get(self.user_id).serialize()["name"],
            "user": User.query.get(self.user_id).serialize(),
            "vehicle": Vehicle.query.get(self.vehicle_id).serialize()
        }

class TokenBlockedList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def serialize(self):
        return {
            "id":self.id,
            "token":self.token,
            "email":self.email,
            "created":self.created_at
        }

# new_favorite = FavoritePeople(user_id= ..... , )
# new_favorite.user.serialize()
# new_favorite.people.serialize()