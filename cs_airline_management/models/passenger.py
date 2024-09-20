import sqlite3

class Passenger:
    def __init__(self, passenger_id, passenger_name, passenger_age):
        self.passenger_id = passenger_id
        self.passenger_name = passenger_name
        self.passenger_age = passenger_age

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO passengers (passenger_id, passenger_name, passenger_age) VALUES (?, ?, ?)",
                       (self.passenger_id, self.passenger_name, self.passenger_age))
        conn.commit()
        conn.close()

    @staticmethod
    def display_passengers():
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM passengers")
        passengers = cursor.fetchall()
        conn.close()

        print("\n--- Passenger Details ---")
        for passenger in passengers:
            print(f"ID: {passenger[0]}, Name: {passenger[1]}, Age: {passenger[2]}")
        print("------------------------")
