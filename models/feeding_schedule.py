class FeedingSchedule:
    def __init__(self, pet_id, feeding_time, food_type):
        self.pet_id = pet_id
        self.feeding_time = feeding_time
        self.food_type = food_type

    def set_schedule(self):
        conn = connect()
        cur = conn.cursor()
        query = """
        INSERT INTO feeding_schedule (pet_id, feeding_time, food_type) 
        VALUES (%s, %s, %s)
        """
        cur.execute(query, (self.pet_id, self.feeding_time, self.food_type))
        conn.commit()
        cur.close()
        conn.close()
        print(f"Feeding schedule for Pet {self.pet_id} set for {self.feeding_time}.")

    @staticmethod
    def view_for_pet(pet_id):
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM feeding_schedule WHERE pet_id = %s", (pet_id,))
        schedules = cur.fetchall()
        cur.close()
        conn.close()
        return schedules
