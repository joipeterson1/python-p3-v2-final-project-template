# lib/models/house_member.py
from models.__init__ import CURSOR, CONN
from models.chore import Chore

class Housemember:

    all = {}

    def __init__(self, name, schedule, chore_id, id=None):
        self.name = name
        self.chore_id = chore_id
        self.schedule = schedule
        self.id = id

    def __repr__(self):
        return (f"<House Member {self.id}: {self.name}, " +
                f"Chore ID: {self.chore_id}, {self.schedule}>"
                )
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
    @property
    def schedule(self):
        return self._schedule
    
    @schedule.setter
    def schedule(self, schedule):
        if isinstance(schedule, str) and len(schedule):
            self._schedule = schedule
        else:
            raise ValueError(
                "Schedule must be a non-empty string"
            )
        
    @property
    def chore_id(self):
        return self._chore_id
    
    @chore_id.setter
    def chore_id(self, chore_id):
        if type(chore_id) is int and Chore.find_by_id(chore_id):
            self._chore_id = chore_id
        else:
            raise ValueError(
                "chore_id must reference a chore in the database"
            )