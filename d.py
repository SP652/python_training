import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect('airline_management.db')
    cursor = conn.cursor()
    
    # Create tables
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

class TicketCounter:
    def __init__(self):
        self.tickets = []

    def book_ticket(self, ticket_id, passenger_id, flight_id, price):
        ticket = {
            'ticket_id': ticket_id,
            'passenger_id': passenger_id,
            'flight_id': flight_id,
            'price': price
        }
        self.tickets.append(ticket)
        self.save_to_db(ticket)

    def save_to_db(self, ticket):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tickets (ticket_id, passenger_id, flight_id, price) VALUES (?, ?, ?, ?)",
                       (ticket['ticket_id'], ticket['passenger_id'], ticket['flight_id'], ticket['price']))
        conn.commit()
        conn.close()

    @staticmethod
    def display_tickets():
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tickets")
        tickets = cursor.fetchall()
        conn.close()

        print("\n--- Ticket Details ---")
        for ticket in tickets:
            print(f"Ticket ID: {ticket[0]}, Passenger ID: {ticket[1]}, Flight ID: {ticket[2]}, Price: {ticket[3]}")
        print("------------------------")

class Employee:
    def __init__(self, employee_id, employee_name, employee_salary, designation, department):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_salary = employee_salary
        self.designation = designation
        self.department = department

    def save_to_db(self):
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO employees (employee_id, employee_name, employee_salary, designation, department) VALUES (?, ?, ?, ?, ?)",
                       (self.employee_id, self.employee_name, self.employee_salary, self.designation, self.department))
        conn.commit()
        conn.close()

    @staticmethod
    def display_employees():
        conn = sqlite3.connect('airline_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        conn.close()

        print("\n--- Employee Details ---")
        for emp in employees:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}, Designation: {emp[3]}, Department: {emp[4]}")
        print("------------------------")

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

def main():
    init_db()

    while True:
        print("\n--- Airline Management System ---")
        print("1. Add Flight")
        print("2. Book Ticket")
        print("3. Add Employee")
        print("4. Add Passenger")
        print("5. Add Runway")
        print("6. Add Luggage")
        print("7. Display Flights")
        print("8. Display Tickets")
        print("9. Display Employees")
        print("10. Display Passengers")
        print("11. Display Runways")
        print("12. Display Luggage")
        print("13. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            flight_id = input("Enter Flight ID: ")
            flight_name = input("Enter Flight Name: ")
            capacity = int(input("Enter Capacity: "))
            starting_time = input("Enter Starting Time (HH:MM): ")
            reaching_time = input("Enter Reaching Time (HH:MM): ")
            source = input("Enter Source: ")
            destination = input("Enter Destination: ")
            price = float(input("Enter Price: "))
            flight = Flight(flight_id, flight_name, capacity, starting_time, reaching_time, source, destination, price)
            flight.save_to_db()
            print(f"Flight {flight_name} added.")

        elif choice == '2':
            ticket_id = input("Enter Ticket ID: ")
            passenger_id = input("Enter Passenger ID: ")
            flight_id = input("Enter Flight ID: ")
            price = float(input("Enter Ticket Price: "))
            ticket_counter = TicketCounter()
            ticket_counter.book_ticket(ticket_id, passenger_id, flight_id, price)
            print(f"Ticket {ticket_id} booked.")

        elif choice == '3':
            employee_id = input("Enter Employee ID: ")
            employee_name = input("Enter Employee Name: ")
            employee_salary = float(input("Enter Employee Salary: "))
            designation = input("Enter Designation: ")
            department = input("Enter Department: ")
            employee = Employee(employee_id, employee_name, employee_salary, designation, department)
            employee.save_to_db()
            print(f"Employee {employee_name} added.")

        elif choice == '4':
            passenger_id = input("Enter Passenger ID: ")
            passenger_name = input("Enter Passenger Name: ")
            passenger_age = int(input("Enter Passenger Age: "))
            passenger = Passenger(passenger_id, passenger_name, passenger_age)
            passenger.save_to_db()
            print(f"Passenger {passenger_name} added.")

        elif choice == '5':
            runway_number = input("Enter Runway Number: ")
            runway = Runway(runway_number)
            runway.save_to_db()
            print(f"Runway {runway_number} added.")

        elif choice == '6':
            luggage_id = input("Enter Luggage ID: ")
            passenger_id = input("Enter Passenger ID: ")
            flight_id = input("Enter Flight ID: ")
            number_of_luggages = int(input("Enter Number of Luggages: "))
            luggage = Luggage(luggage_id, passenger_id, flight_id, number_of_luggages)
            luggage.save_to_db()
            print(f"Luggage {luggage_id} added.")

        elif choice == '7':
            Flight.display_flights()

        elif choice == '8':
            TicketCounter.display_tickets()

        elif choice == '9':
            Employee.display_employees()

        elif choice == '10':
            Passenger.display_passengers()

        elif choice == '11':
            Runway.display_runways()

        elif choice == '12':
            Luggage.display_luggage()

        elif choice == '13':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
