import sqlite3
from datetime import datetime

class DataLog:
    def __init__(self, raw_data, processed_data):
        self.raw_data = raw_data
        self.processed_data = processed_data
        self.timestamp = datetime.now().isoformat()

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO data_logs (raw_data, processed_data, timestamp) VALUES (?, ?, ?)",
                       (self.raw_data, self.processed_data, self.timestamp))
        conn.commit()
        conn.close()

    @staticmethod
    def display_data_logs():
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data_logs")
        logs = cursor.fetchall()
        conn.close()

        print("\n--- Data Log Details ---")
        for log in logs:
            print(f"ID: {log[0]}, Raw Data: {log[1]}, Processed Data: {log[2]}, Timestamp: {log[3]}")
        print("------------------------")
