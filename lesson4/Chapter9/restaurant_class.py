print("-------------Excercise 9-1-------------")

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

restaurant = Restaurant("Qdoba","Mexican Eats")
print("The restaurant name is", restaurant.restaurant_name)
print("The restaurant cuisine type is", restaurant.cuisine_type)
restaurant.open_restaurant()
restaurant.describe_restaurant()

print("-------------Excercise 9-2-------------")
restaurant1 = Restaurant("Culver's","American")
restaurant2 = Restaurant("Olive Garden","Italian")
restaurant3 = Restaurant("Golden Chopsticks","Chinese")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
