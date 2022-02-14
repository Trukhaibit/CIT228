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
