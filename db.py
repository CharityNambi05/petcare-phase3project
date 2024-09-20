import psycopg2

def connect():
    """Establish connection to the PostgreSQL database"""
    conn = psycopg2.connect(
        dbname="pet_care", 
        user="charity", 
        password="Lola@123", 
        host="localhost", 
        port="5432"
    )
    return conn
