from db import connect
from psycopg2 import sql

class Pet:
    def __init__(self, name, species, breed, age, owner_name):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.owner_name = owner_name

    def save(self):
        conn = connect()
        cur = conn.cursor()
        query = """
        INSERT INTO pets (name, species, breed, age, owner_name) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(query, (self.name, self.species, self.breed, self.age, self.owner_name))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Pet {self.name} added successfully!")

    @staticmethod
    def view_all():
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM pets")
        pets = cur.fetchall()
        cur.close()
        conn.close()
        return pets

    @staticmethod
    def update(pet_id, **kwargs):
        conn = connect()
        cur = conn.cursor()
        for column, value in kwargs.items():
            query = sql.SQL("UPDATE pets SET {column} = %s WHERE id = %s").format(column=sql.Identifier(column))
            cur.execute(query, (value, pet_id))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Pet {pet_id} updated successfully!")

    @staticmethod
    def delete(pet_id):
        conn = connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM pets WHERE id = %s", (pet_id,))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Pet {pet_id} deleted successfully!")
