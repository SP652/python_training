# booking_service.py
import csv
from datetime import datetime
import os

class BookingService:
    def __init__(self, csv_file='bookings.csv'):
        self.bookings = []  # List to keep track of bookings
        self.csv_file = csv_file
        self.ensure_csv_headers()

    def ensure_csv_headers(self):
        # Check if CSV file exists, if not, create it with headers
        if not os.path.isfile(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Flight ID', 'Source', 'Destination', 'Departure Time', 'Arrival Time', 'Fare', 'Passenger Name', 'Email', 'Timestamp', 'Cancellation Status'])

    def record_booking(self, flight, name, email):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        booking_info = {'Flight': flight, 'Name': name, 'Email': email, 'Timestamp': timestamp, 'Cancelled': False}
        self.bookings.append(booking_info)  # Store booking info in the list
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([flight.flight_id, flight.source, flight.destination, flight.departure_time, flight.arrival_time, flight.fare, name, email, timestamp, 'No'])

    def update_booking_status(self, email, cancelled=True):
        # Update the CSV file to reflect the cancellation status
        rows = []
        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows.append(header)  # Preserve header
            for row in reader:
                if row[7] == email:
                    row[-1] = 'Yes' if cancelled else 'No'  # Update cancellation status
                rows.append(row)
        
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
