import sqlite3

class Device:
    def __init__(self, device_id, device_name, ip_address, protocol_type):
        self.device_id = device_id
        self.device_name = device_name
        self.ip_address = ip_address
        self.protocol_type = protocol_type
        self.status = "Operational"

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO devices (id, name, ip_address, protocol, status) VALUES (?, ?, ?, ?, ?)",
                       (self.device_id, self.device_name, self.ip_address, self.protocol_type, self.status))
        conn.commit()
        conn.close()

    @staticmethod
    def display_devices():
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM devices")
        devices = cursor.fetchall()
        conn.close()

        print("\n--- Device Details ---")
        for device in devices:
            print(f"ID: {device[0]}, Name: {device[1]}, IP: {device[2]}, Protocol: {device[3]}, Status: {device[4]}")
        print("------------------------")
