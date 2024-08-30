#!/usr/bin/env python3

import sqlite3

CONN = sqlite3.connect('chore.db')
CURSOR = CONN.cursor()
from models.chore import Chore
from models.house_member import Housemember
import ipdb

def reset_database():
    Chore.drop_table()
    Housemember.drop_table()
    Chore.create_table()
    Housemember.create_table

    dishes = Chore.create("Dishes", "Everyday", "Kitchen")
    laundry = Chore.create("Laundry", "SaSu", "Laundry Room")
    Housemember.create("Joi", 26, dishes.id)
    Housemember.create("Malik", 27, laundry.id)

reset_database()
ipdb.set_trace()
