class Car():
    """A simple attempt to resprest a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formated descrriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Pinrt a statement shwoing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increament_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Mileage cannot be incremented with a negative value")


my_new_car = Car('audi', 'a4', 2017)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(24)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23400)
my_used_car.read_odometer()
my_used_car.increament_odometer(100)
my_used_car.read_odometer()
