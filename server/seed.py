#!/usr/bin/env python3
#server/seed.py

# to get randomized data
from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():

    # initialize a fake generator
    fake = Faker()

    # delete the rows in the "pets" table
    Pet.query.delete()

    # Create an empty list
    pets = []

    species =['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Add some pet instance to the list
    for n in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()