import sqlite3

class Transfer:
    def __init__(self, transfer_id, source_path, destination_path):
        self.transfer_id = transfer_id
        self.source_path = source_path
        self.destination_path = destination_path
        self.status = "Pending"

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO transfers (id, source_path, destination_path, status) VALUES (?, ?, ?, ?)",
                       (self.transfer_id, self.source_path, self.destination_path, self.status))
        conn.commit()
        conn.close()

    @staticmethod
    def display_transfers():
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transfers")
        transfers = cursor.fetchall()
        conn.close()

        print("\n--- Transfer Details ---")
        for transfer in transfers:
            print(f"ID: {transfer[0]}, Source: {transfer[1]}, Destination: {transfer[2]}, Status: {transfer[3]}")
        print("------------------------")
