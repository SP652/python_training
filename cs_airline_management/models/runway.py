import sqlite3

class Runway:
    def __init__(self, runway_number):
        self.runway_number = runway_number
        self.flight_name = None
        self.occupied_status = "Free"

    def occupy(self, flight_name):
        self.flight_name = flight_name
        self.occupied_status = "Occupied"

    def free(self):
        self.flight_name = None
        self.occupied_status = "Free"

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO runways (runway_number, flight_name, occupied_status) VALUES (?, ?, ?)",
                       (self.runway_number, self.flight_name, self.occupied_status))
        conn.commit()
        conn.close()

    @staticmethod
    def display_runways():
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM runways")
        runways = cursor.fetchall()
        conn.close()

        print("\n--- Runway Details ---")
        for runway in runways:
            print(f"Runway Number: {runway[0]}, Flight Name: {runway[1]}, Status: {runway[2]}")
        print("------------------------")
