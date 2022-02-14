from restaurant import Restaurant
from icecream import IceCreamStand

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