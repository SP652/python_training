import sqlite3

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

    cursor.execute('''CREATE TABLE IF NOT EXISTS flights (
                        flight_id TEXT PRIMARY KEY,
                        flight_name TEXT,
                        capacity INTEGER,
                        starting_time TEXT,
                        reaching_time TEXT,
                        source TEXT,
                        destination TEXT,
                        price REAL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tickets (
                        ticket_id TEXT PRIMARY KEY,
                        passenger_id TEXT,
                        flight_id TEXT,
                        price REAL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                        employee_id TEXT PRIMARY KEY,
                        employee_name TEXT,
                        employee_salary REAL,
                        designation TEXT,
                        department TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS passengers (
                        passenger_id TEXT PRIMARY KEY,
                        passenger_name TEXT,
                        passenger_age INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS runways (
                        runway_number TEXT PRIMARY KEY,
                        flight_name TEXT,
                        occupied_status TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS luggage (
                        luggage_id TEXT PRIMARY KEY,
                        passenger_id TEXT,
                        flight_id TEXT,
                        number_of_luggages INTEGER)''')

    conn.commit()
    conn.close()
