#!/usr/bin/env python3
# Author ID: lbrown63

class Vehicle:
    """A class representing a vehicle with make, model, and year attributes."""
    
    def __init__(self, make, model, year):
        """Constructor to initialize a vehicle object."""
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        """Returns a formatted string with vehicle information."""
        return f"{self.year} {self.make} {self.model}"

if __name__ == '__main__':
    car1 = Vehicle("Toyota", "Corolla", 2020)
    car2 = Vehicle("Honda", "Civic", 2021)
    
    print(car1.get_info())
    print(car2.get_info())
