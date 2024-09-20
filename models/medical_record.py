from db import connect

class MedicalRecord:
    def __init__(self, pet_id, record_date, notes):
        self.pet_id = pet_id
        self.record_date = record_date
        self.notes = notes

    def log(self):
        conn = connect()
        cur = conn.cursor()
        query = """
        INSERT INTO medical_records (pet_id, record_date, notes) 
        VALUES (%s, %s, %s)
        """
        cur.execute(query, (self.pet_id, self.record_date, self.notes))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Medical record for Pet {self.pet_id} logged on {self.record_date}.")

    @staticmethod
    def view_for_pet(pet_id):
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM medical_records WHERE pet_id = %s", (pet_id,))
        records = cur.fetchall()
        cur.close()
        conn.close()
        return records
