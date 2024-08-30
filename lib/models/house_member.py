#!/usr/bin/env python3
import sqlite3

CONN = sqlite3.connect('chore.db')
CURSOR = CONN.cursor()

from models.chore import Chore

class Housemember:

    all = {}

    def __init__(self, name, age, chore_id, id=None):
        self.name = name
        self.age = age
        self.chore_id = chore_id
        self.id = id

    def __repr__(self):
        return (f"<House Member {self.id}: {self.name}, " +
                f"{self.name} is {self.age} years old, " +
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
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and (age > 5):
            self._age = age
        else:
            raise ValueError(
                "The House member must be 6 or older to be assigned a chore."
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
            age INTEGER,
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
            INSERT INTO house_members (name, age, chore_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.age, self.chore_id))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, age, chore_id):
            house_member = cls(name, age, chore_id)
            house_member.save()
            return house_member
    
    def update(self):
        sql = """
            UPDATE house_members
            SET name = ?, age = ?, chore_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age, self.chore_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM house_members
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        house_member = cls.all.get(row[0])
        if house_member:
            house_member.name = row[1]
            house_member.age = row[2]
            house_member.chore_id = row[3]
        else:
            house_member = cls(row[1], row[2], row[3])
            house_member.id = row[0]
            cls.all[house_member.id] = house_member
        return house_member
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM house_members
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM house_members
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id, )).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM house_members
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def renumber_ids(cls):
        sql = """
            SELECT id FROM house_members ORDER BY id
        """
        ids = CURSOR.execute(sql).fetchall()
        for index, (id,) in enumerate(ids):
            new_id = index + 1
            sql = """
                UPDATE house_members
                SET id = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (new_id, id))
            CONN.commit()


