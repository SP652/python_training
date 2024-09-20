import sqlite3

class Luggage:
    def __init__(self, luggage_id, passenger_id, flight_id, number_of_luggages):
        self.luggage_id = luggage_id
        self.passenger_id = passenger_id
        self.flight_id = flight_id
        self.number_of_luggages = number_of_luggages

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO luggage (luggage_id, passenger_id, flight_id, number_of_luggages) VALUES (?, ?, ?, ?)",
                       (self.luggage_id, self.passenger_id, self.flight_id, self.number_of_luggages))
        conn.commit()
        conn.close()

    @staticmethod
    def display_luggage():
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM luggage")
        luggages = cursor.fetchall()
        conn.close()

        print("\n--- Luggage Details ---")
        for luggage in luggages:
            print(f"Luggage ID: {luggage[0]}, Passenger ID: {luggage[1]}, Flight ID: {luggage[2]}, Number of Luggages: {luggage[3]}")
        print("------------------------")
