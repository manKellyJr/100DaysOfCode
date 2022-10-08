class Restaurant():
    """A class that models a Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name + ". It offers cuisine type of " + self.cuisine_type)


    def open_restaurant(self):
        print(self.restaurant_name + " is now open")

my_restaurant = Restaurant("Ratatoui", "French Chicken Cuisine")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
