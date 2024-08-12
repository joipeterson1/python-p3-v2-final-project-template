#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
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
    Housemember.create("Joi", dishes)
    Housemember.create("Malik", laundry)

reset_database()
ipdb.set_trace()
