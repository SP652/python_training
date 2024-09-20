import smtplib
import requests
import threading
import time
import sqlite3
from datetime import datetime

# Database setup
def init_db():
    conn = sqlite3.connect('airline_management.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS devices (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        ip_address TEXT,
                        protocol TEXT,
                        status TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS transfers (
                        id TEXT PRIMARY KEY,
                        source_path TEXT,
                        destination_path TEXT,
                        status TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS alerts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        message TEXT,
                        timestamp TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS data_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        raw_data TEXT,
                        processed_data TEXT,
                        timestamp TEXT)''')

    conn.commit()
    conn.close()

class NetworkManagement:
    def __init__(self, network_name, location):
        self.network_name = network_name
        self.location = location
        self.network_status = "Operational"
        self.devices = []
        self.alert_system = AlertSystem()

    def monitor(self):
        print(f"Monitoring network: {self.network_name}")
        for device in self.devices:
            device.get_status()
            time.sleep(1)

    def shutdown(self):
        self.network_status = "Down"
        print(f"Network {self.network_name} is down.")

    def add_device(self, device):
        self.devices.append(device)
        device.save_to_db()

class Device:
    def __init__(self, device_id, device_name, ip_address, protocol_type):
        self.device_id = device_id
        self.device_name = device_name
        self.ip_address = ip_address
        self.protocol_type = protocol_type
        self.status = "Operational"

    def connect(self):
        print(f"Connecting to {self.device_name} at {self.ip_address}")
        return True

    def get_status(self):
        if self.connect():
            print(f"{self.device_name} is {self.status}")
        else:
            self.status = "Down"
            print(f"{self.device_name} is {self.status}")

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO devices (id, name, ip_address, protocol, status) VALUES (?, ?, ?, ?, ?)",
                       (self.device_id, self.device_name, self.ip_address, self.protocol_type, self.status))
        conn.commit()
        conn.close()

class FileTransfer:
    def __init__(self, transfer_id, source_path, destination_path):
        self.transfer_id = transfer_id
        self.source_path = source_path
        self.destination_path = destination_path
        self.status = "Pending"

    def initiate_transfer(self):
        print(f"Initiating transfer from {self.source_path} to {self.destination_path}")
        time.sleep(2)  # Simulating time taken for transfer
        self.status = "Completed"
        print(f"Transfer {self.transfer_id} completed.")
        self.save_to_db()

    def check_status(self):
        print(f"Transfer {self.transfer_id} status: {self.status}")

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transfers (id, source_path, destination_path, status) VALUES (?, ?, ?, ?)",
                       (self.transfer_id, self.source_path, self.destination_path, self.status))
        conn.commit()
        conn.close()

class AlertSystem:
    def __init__(self):
        self.alerts = []

    def send_email(self, message):
        print("Sending alert email...")
        print(f"Email sent with message: {message}")

    def log_alert(self, alert):
        self.alerts.append(alert)
        self.send_email(alert)
        self.save_to_db(alert)

    def save_to_db(self, message):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alerts (message, timestamp) VALUES (?, ?)",
                       (message, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()

class DataProcessor:
    def __init__(self):
        self.data_storage = []

    def process_data(self, raw_data):
        print(f"Processing data: {raw_data}")
        processed_data = raw_data.upper()
        self.store_data(raw_data, processed_data)
        return processed_data

    def store_data(self, raw_data, processed_data):
        self.data_storage.append(processed_data)
        print(f"Data stored: {processed_data}")
        self.save_to_db(raw_data, processed_data)

    def save_to_db(self, raw_data, processed_data):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO data_logs (raw_data, processed_data, timestamp) VALUES (?, ?, ?)",
                       (raw_data, processed_data, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.scraped_data = None

    def scrape(self):
        print(f"Scraping data from {self.url}")
        self.scraped_data = "Sample scraped data"
        return self.scraped_data

    def extract_data(self):
        if self.scraped_data:
            print(f"Extracted data: {self.scraped_data}")
            return self.scraped_data
        return None

# Example usage

if __name__ == "__main__":
    # Initialize the database
    init_db()

    # Create network management system
    network = NetworkManagement("Airline Network", "New York")

    # Add devices
    device1 = Device("D1", "Router 1", "192.168.1.1", "SNMP")
    device2 = Device("D2", "Switch 1", "192.168.1.2", "SSH")

    network.add_device(device1)
    network.add_device(device2)

    # Start monitoring network
    monitoring_thread = threading.Thread(target=network.monitor)
    monitoring_thread.start()

    # File Transfer Example
    transfer = FileTransfer("T1", "/path/to/source/file.txt", "/path/to/destination/file.txt")
    transfer.initiate_transfer()
    transfer.check_status()

    # Data Processing Example
    processor = DataProcessor()
    raw_data = "network log data"
    processed_data = processor.process_data(raw_data)

    # Web Scraping Example
    scraper = WebScraper("http://example.com/network-status")
    scraped_data = scraper.scrape()
    scraper.extract_data()

    # Join monitoring thread
    monitoring_thread.join()
