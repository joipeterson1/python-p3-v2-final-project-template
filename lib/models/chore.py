# lib/models/chore.py
from .__init__ import CURSOR, CONN

class Chore:
    
    all = {}

    def __init__(self, name, schedule, location, id=None):
        self.name = name
        self.schedule = schedule
        self.location = location
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
            CREATE TABLE IF NOT EXISTS chores (
            id INTEGER PRIMARY KEY,
            name TEXT,
            schedule TEXT,
            location TEXT
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
        CURSOR.execute(sql, (self.name, self.schedule, self.location))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, schedule, location):
        chore = cls(name, schedule, location)
        chore.save()
        return chore
    
    def update(self):
        sql = """
            UPDATE chores
            SET name = ?, schedule = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.schedule, self.location))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM chores
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        chore = cls.all.get(row[0])
        if chore:
            chore.name = row[1]
            chore.schedule = row[2]
            chore.location = row[3]
        else:
            chore = cls(row[1], row[2], row[3])
            chore.id = row[0]
            cls.all[chore.id] = chore
            return chore
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM chores
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, _id):
        sql = """
            SELECT *
            FROM chores
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (_id, )).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM chores
            WHERE name is ?
        """
        row = CURSOR.execute(sql (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_schedule(cls, schedule):
        sql = """
            SELECT *
            FROM chores
            WHERE schedule is ?
        """
        row = CURSOR.execute(sql (schedule,)).fetchall()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_location(cls, location):
        sql = """
            SELECT *
            FROM chores
            WHERE location is ?
        """
        row = CURSOR.execute(sql (location,)).fetchall()
        return cls.instance_from_db(row) if row else None

    def house_members(self):
        from models.house_member import Housemember
        sql = """
            SELECT * from house_members
            WHERE chores_id = ?
        """
        CURSOR.execute(sql (self.id,),)
        rows = CURSOR.fetchall()
        return [
            Housemember.instance_from_db(row) for row in rows
        ]
    


