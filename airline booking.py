class Flight:
    def __init__(self, flight_number, source, destination, departure_time, arrival_time, available_seats):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.available_seats = available_seats


class BookingSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, source, destination):
        available_flights = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination and flight.available_seats > 0:
                available_flights.append(flight)
        return available_flights

    def book_flight(self, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                if flight.available_seats > 0:
                    flight.available_seats -= 1
                    print("Booking successful!")
                else:
                    print("No available seats for this flight.")
                return
        print("Flight not found.")


# Create a booking system
booking_system = BookingSystem()

# Create some flights
flight1 = Flight("F001", "New York", "London", "10:00", "16:00", 50)
flight2 = Flight("F002", "London", "Paris", "12:00", "14:00", 20)
flight3 = Flight("F003", "Tokyo", "Sydney", "08:00", "18:00", 100)

# Add flights to the booking system
booking_system.add_flight(flight1)
booking_system.add_flight(flight2)
booking_system.add_flight(flight3)

# Search flights from New York to London
available_flights = booking_system.search_flights("New York", "London")
print("Available flights from New York to London:")
for flight in available_flights:
    print(f"Flight: {flight.flight_number}, Departure: {flight.departure_time}, Arrival: {flight.arrival_time}")

# Book a flight
flight_number = input("Enter the flight number to book: ")
booking_system.book_flight(flight_number)
