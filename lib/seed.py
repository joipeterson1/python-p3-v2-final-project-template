#!/usr/bin/env python3

import sqlite3

CONN = sqlite3.connect('chore.db')
CURSOR = CONN.cursor()
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


    Housemember.create("Joi", 26, dishes.id)
    Housemember.create("Malik", 27, laundry.id)

    print("Housemembers in the database:", Housemember.all)

if __name__ == "__main__":
    seed_database()
print("The database has been seeded!")
