# flight_management_system.py
from getpass import getpass
from flight import Flight
from email_service import send_email_confirmation, send_cancellation_email
from booking_service import BookingService

class FlightManagementSystem:
    def __init__(self):
        self.flights = []
        self.booking_service = BookingService()
        self.admin_logged_in = False
    
    def admin_login(self):
        username = input("Enter admin username: ")
        password = getpass("Enter admin password: ")
        if username == "admin" and password == "password":  # Replace with secure handling
            self.admin_logged_in = True
            print("Admin logged in successfully.")
        else:
            print("Invalid credentials.")
    
    def add_flight(self):
        if not self.admin_logged_in:
            print("Access denied. Admin login required.")
            return
        flight_id = input("Enter Flight ID: ")
        source = input("Enter Source: ")
        destination = input("Enter Destination: ")
        departure_time = input("Enter Departure Time: ")
        arrival_time = input("Enter Arrival Time: ")
        fare = float(input("Enter Fare: "))
        flight = Flight(flight_id, source, destination, departure_time, arrival_time, fare)
        self.flights.append(flight)
        print("Flight added successfully.")

    def delete_flight(self):
        if not self.admin_logged_in:
            print("Access denied. Admin login required.")
            return
        flight_id = input("Enter Flight ID to delete: ")
        flight = next((f for f in self.flights if f.flight_id == flight_id), None)
        if flight:
            self.flights.remove(flight)
            print("Flight deleted successfully.")
        else:
            print("Flight not found.")

    def display_flights(self):
        if not self.flights:
            print("No flights available.")
            return
        print("\nCurrent Flight Details:")
        print("{:<15} {:<15} {:<15} {:<20} {:<20} {:<10}".format("Flight ID", "Source", "Destination", "Departure Time", "Arrival Time", "Fare"))
        for flight in self.flights:
            print("{:<15} {:<15} {:<15} {:<20} {:<20} ${:<10}".format(flight.flight_id, flight.source, flight.destination, flight.departure_time, flight.arrival_time, flight.fare))

    def book_flight(self):
        flight_id = input("Enter Flight ID for booking: ")
        flight = next((f for f in self.flights if f.flight_id == flight_id), None)
        if not flight:
            print("Flight not found.")
            return
        
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        
        send_email_confirmation(name, email, flight)
        self.booking_service.record_booking(flight, name, email)  # Pass the flight object
        print("Booking successful! A confirmation email has been sent.")

    def cancel_booking(self):
        email = input("Enter your email to cancel booking: ")
        booking = next((b for b in self.booking_service.bookings if b['Email'] == email), None)
        if booking:
            send_cancellation_email(booking['Name'], email, booking['Flight'])
            self.booking_service.update_booking_status(email, cancelled=True)  # Update CSV with cancellation status
            self.booking_service.bookings.remove(booking)  # Remove from active bookings
            print("Booking cancelled successfully. A cancellation email has been sent.")
        else:
            print("No booking found for this email.")

    def logout(self):
        self.admin_logged_in = False
        print("Logged out successfully.")

    def run(self):
        self.admin_login()
        while self.admin_logged_in:
            print("\nOptions: 1. Add Flight 2. Delete Flight 3. Display Flights 4. Book Flight 5. Cancel Booking 6. Logout")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_flight()
            elif choice == '2':
                self.delete_flight()
            elif choice == '3':
                self.display_flights()
            elif choice == '4':
                self.book_flight()
            elif choice == '5':
                self.cancel_booking()
            elif choice == '6':
                self.logout()
            else:
                print("Invalid option.")

if __name__ == "__main__":
    system = FlightManagementSystem()
    system.run()
