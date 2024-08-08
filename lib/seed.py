#!/usr/bin/env python3
# lib/seed.py

from models.__init__ import CONN, CURSOR
from models.chore import Chore
from models.house_member import Housemember


def seed_database():
    Chore.drop_table()
    Housemember.drop_table()
    Chore.create_table()
    Housemember.create_table()

    dishes = Chore.create("Dishes", "Everyday", "Kitchen")
    laundry = Chore.create("Laundry", "SaSu", "Laundry Room")

    print("Chores in the database:", Chore.all)


    Housemember.create("Joi", dishes.id)
    Housemember.create("Malik", laundry.id)

seed_database()
print("The database has been seeded!")
