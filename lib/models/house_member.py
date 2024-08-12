#!/usr/bin/env python3
from .__init__ import CURSOR, CONN
from .chore import Chore

class Housemember:

    all = {}

    def __init__(self, name, chore_id, id=None):
        self.name = name
        self.chore_id = chore_id
        self.id = id

    def __repr__(self):
        return (f"<House Member {self.id}: {self.name}, " +
                f"Chore ID: {self.chore_id}>"
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
        
    @classmethod
    def create_table(cls):
       sql= """
            CREATE TABLE IF NOT EXISTS house_members(
            id INTEGER PRIMARY KEY,
            name TEXT,
            chore_id INTEGER,
            FOREIGN KEY (chore_id) REFERENCES chores(id)
        )
        """
       CURSOR.execute(sql)
       CONN.commit()

    @classmethod
    def drop_table(cls):
        sql= """
            DROP TABLE IF EXISTS house_members;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql= """
            INSERT INTO house_members (name, chore_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql)
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, chore_id):
            house_member = cls(name, chore_id)
            house_member.save()
            return house_member
    
    def update(self):
        sql = """
            UPDATE house_member
            SET name = ?, chore_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.chore_id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM house_member
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        chore = cls.all.get(row[0])
        if chore:
            chore.name = row[1]
            chore.chore_id = row[2]
        else:
            chore = cls(row[1], row[2])
            chore.id = row[0]
            cls.all[chore.id] = chore
            return chore
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM house_member
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM house_member
            WHERE id = ?
        """
        row = CURSOR.execute(sql(id, )).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM house_member
            WHERE name is ?
        """
        row = CURSOR.execute(sql (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    


