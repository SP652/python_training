# flight.py
class Flight:
    def __init__(self, flight_id, source, destination, departure_time, arrival_time, fare):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.fare = fare
