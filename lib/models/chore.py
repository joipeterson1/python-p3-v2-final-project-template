# lib/models/chore.py
from models.__init__ import CURSOR, CONN

class Chore:
    
    all = {}

    def __init__(self, name, location, schedule, id=None):
        self.name = name
        self.location = location
        self.schedule = schedule
        self.id = id

    def __repr__(self):
        return (f"<Chore {self.id}: {self.name}, " +
                f"Location: {self.location}, {self.schedule}>"
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
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError(
                "location must be a non-empty string"
            )
        
    @classmethod
    def create_table(cls):
       sql= """
            CREATE TABLE IF NOT EXIST chores(
            id INTEGER PRIMARY KEY,
            name TEXT,
            schedule TEXT,
            location TEXT,
        )
        """
       CURSOR.execute(sql)
       CONN.commit()

    @classmethod
    def drop_table(cls):
        sql= """
            DROP TABLE IF EXISTS chores;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql= """
            INSERT INTO chores (name, schedule, location)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql)
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self