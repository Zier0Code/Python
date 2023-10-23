class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ['add','adde','addere','earwad',"sad"]

for person in people:
    if flight.add_passengers(person):
        print(f"Added {person} into the flight successfully")
    else:
        print(f"No more Seats Available for {person}")