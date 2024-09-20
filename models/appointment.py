from db import connect

class Appointment:
    def __init__(self, pet_id, appointment_date, description):
        self.pet_id = pet_id
        self.appointment_date = appointment_date
        self.description = description

    def schedule(self):
        conn = connect()
        cur = conn.cursor()
        query = """
        INSERT INTO appointments (pet_id, appointment_date, description) 
        VALUES (%s, %s, %s)
        """
        cur.execute(query, (self.pet_id, self.appointment_date, self.description))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Appointment for Pet {self.pet_id} scheduled on {self.appointment_date}.")

    @staticmethod
    def view_for_pet(pet_id):
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM appointments WHERE pet_id = %s", (pet_id,))
        appointments = cur.fetchall()
        cur.close()
        conn.close()
        return appointments
