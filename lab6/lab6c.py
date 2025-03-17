#!/usr/bin/env python3
# Author ID: lbrown63

class Temperature:
    """A class representing temperature in Celsius."""
    
    def __init__(self, celsius):
        """Constructor to initialize temperature, validating input."""
        if not isinstance(celsius, (int, float)):
            raise ValueError("Temperature must be a number.")
        self.celsius = celsius

    def to_fahrenheit(self):
        """Converts Celsius to Fahrenheit."""
        return (self.celsius * 9/5) + 32

    def set_temperature(self, new_temp):
        """Sets a new temperature with error handling."""
        if not isinstance(new_temp, (int, float)):
            return "Error: Temperature must be a number."
        self.celsius = new_temp
        return f"Temperature set to {self.celsius}°C"

if __name__ == '__main__':
    try:
        temp1 = Temperature(25)
        print(f"Temperature in Fahrenheit: {temp1.to_fahrenheit()}°F")

        print(temp1.set_temperature(30))
        print(temp1.set_temperature("Hot"))  # Should return an error message
    except ValueError as e:
        print(e)
