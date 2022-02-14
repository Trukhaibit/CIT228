class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}")
        print(f"It has served {self.number_served} customers")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self):
        self.number_served = int(input("Customers Served:"))

    def increment_number_served(self):
        self.number_served += int(input("New Customers Served:"))
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ["Vanilla","Strawberry","Chocolate","Superman"]

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

print("-------------Excercise 9-1-------------")
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

print("-------------Excercise 9-4-------------")
restaurant = Restaurant("McDonald's","American")
restaurant.describe_restaurant()
restaurant.number_served = 12
restaurant.describe_restaurant()
restaurant.set_number_served()
restaurant.describe_restaurant()
restaurant.increment_number_served()
restaurant.describe_restaurant()

print("-------------Excercise 9-6-------------")
iceCreamStand = IceCreamStand("Moomers","Ice Cream")
iceCreamStand.display_flavors()
