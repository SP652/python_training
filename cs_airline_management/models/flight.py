import sqlite3

class Flight:
    def __init__(self, flight_id, flight_name, capacity, starting_time, reaching_time, source, destination, price):
        self.flight_id = flight_id
        self.flight_name = flight_name
        self.capacity = capacity
        self.starting_time = starting_time
        self.reaching_time = reaching_time
        self.source = source
        self.destination = destination
        self.price = price

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO flights (flight_id, flight_name, capacity, starting_time, reaching_time, source, destination, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (self.flight_id, self.flight_name, self.capacity, self.starting_time, self.reaching_time, self.source, self.destination, self.price))
        conn.commit()
        conn.close()

    @staticmethod
    def display_flights():
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM flights")
        flights = cursor.fetchall()
        conn.close()

        print("\n--- Flight Details ---")
        for flight in flights:
            print(f"ID: {flight[0]}, Name: {flight[1]}, Capacity: {flight[2]}, Start: {flight[3]}, Reach: {flight[4]}, Source: {flight[5]}, Destination: {flight[6]}, Price: {flight[7]}")
        print("------------------------")
