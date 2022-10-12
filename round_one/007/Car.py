class Car():
    """A simple attempt to resprest a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        """Return a neatly formated descrriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Pinrt a statement shwoing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it")

my_new_car = Car('audi', 'a4', 2017)
print(my_new_car.get_description())
my_new_car.read_odometer()
