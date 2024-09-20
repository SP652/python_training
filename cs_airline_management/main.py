from database import init_db
from models.network_management import NetworkManagement
from models.device import Device
from models.flight import Flight
from models.ticket import TicketCounter
from models.employee import Employee
from models.passenger import Passenger
from models.runway import Runway
from models.luggage import Luggage
from models.transfer import Transfer
from models.alert import Alert
from models.data_log import DataLog

def main():
    init_db()
    network = NetworkManagement("Main Network", "Central Airport")

    while True:
        print("\n--- Airline Management System ---")
        print("1. Add Device")
        print("2. Add Flight")
        print("3. Book Ticket")
        print("4. Add Employee")
        print("5. Add Passenger")
        print("6. Add Runway")
        print("7. Add Luggage")
        print("8. Display Flights")
        print("9. Display Tickets")
        print("10. Display Employees")
        print("11. Display Passengers")
        print("12. Display Runways")
        print("13. Display Luggage")
        print("14. Display Devices")
        print("15. Add Transfer")
        print("16. Display Transfers")
        print("17. Add Alert")
        print("18. Display Alerts")
        print("19. Add Data Log")
        print("20. Display Data Logs")
        print("21. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            device_id = input("Enter Device ID: ")
            device_name = input("Enter Device Name: ")
            ip_address = input("Enter IP Address: ")
            protocol_type = input("Enter Protocol Type: ")
            device = Device(device_id, device_name, ip_address, protocol_type)
            network.add_device(device)
            print(f"Device {device_name} added.")

        elif choice == '2':
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

        elif choice == '3':
            ticket_id = input("Enter Ticket ID: ")
            passenger_id = input("Enter Passenger ID: ")
            flight_id = input("Enter Flight ID: ")
            price = float(input("Enter Ticket Price: "))
            ticket_counter = TicketCounter()
            ticket_counter.book_ticket(ticket_id, passenger_id, flight_id, price)
            print(f"Ticket {ticket_id} booked.")

        elif choice == '4':
            employee_id = input("Enter Employee ID: ")
            employee_name = input("Enter Employee Name: ")
            employee_salary = float(input("Enter Salary: "))
            designation = input("Enter Designation: ")
            department = input("Enter Department: ")
            employee = Employee(employee_id, employee_name, employee_salary, designation, department)
            employee.save_to_db()
            print(f"Employee {employee_name} added.")

        elif choice == '5':
            passenger_id = input("Enter Passenger ID: ")
            passenger_name = input("Enter Passenger Name: ")
            passenger_age = int(input("Enter Passenger Age: "))
            passenger = Passenger(passenger_id, passenger_name, passenger_age)
            passenger.save_to_db()
            print(f"Passenger {passenger_name} added.")

        elif choice == '6':
            runway_number = input("Enter Runway Number: ")
            runway = Runway(runway_number)
            runway.save_to_db()
            print(f"Runway {runway_number} added.")

        elif choice == '7':
            luggage_id = input("Enter Luggage ID: ")
            passenger_id = input("Enter Passenger ID: ")
            flight_id = input("Enter Flight ID: ")
            number_of_luggages = int(input("Enter Number of Luggages: "))
            luggage = Luggage(luggage_id, passenger_id, flight_id, number_of_luggages)
            luggage.save_to_db()
            print(f"Luggage {luggage_id} added.")

        elif choice == '8':
            Flight.display_flights()

        elif choice == '9':
            TicketCounter.display_tickets()

        elif choice == '10':
            Employee.display_employees()

        elif choice == '11':
            Passenger.display_passengers()

        elif choice == '12':
            Runway.display_runways()

        elif choice == '13':
            Luggage.display_luggage()

        elif choice == '14':
            Device.display_devices()

        elif choice == '15':
            transfer_id = input("Enter Transfer ID: ")
            source_path = input("Enter Source Path: ")
            destination_path = input("Enter Destination Path: ")
            transfer = Transfer(transfer_id, source_path, destination_path)
            transfer.save_to_db()
            print(f"Transfer {transfer_id} added.")

        elif choice == '16':
            Transfer.display_transfers()

        elif choice == '17':
            message = input("Enter Alert Message: ")
            alert = Alert(message)
            alert.save_to_db()

            # Send email alert
            to_email = input("Enter recipient email address for alert: ")
            alert.send_email_alert(to_email)
            print("Alert added.")


        elif choice == '18':
            Alert.display_alerts()

        elif choice == '19':
            raw_data = input("Enter Raw Data: ")
            processed_data = input("Enter Processed Data: ")
            data_log = DataLog(raw_data, processed_data)
            data_log.save_to_db()
            print("Data Log added.")

        elif choice == '20':
            DataLog.display_data_logs()

        elif choice == '21':
            print("Exiting...")
            break

if __name__ == '__main__':
    main()
