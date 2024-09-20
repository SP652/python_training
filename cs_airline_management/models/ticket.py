import sqlite3

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
