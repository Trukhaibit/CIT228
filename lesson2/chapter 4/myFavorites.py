print("----------------Hands on 1----------------")
foods=["Stroganoff","Cordon Bleu","Sherbet","Pop", "Fudge","Deep-Dish"]
numbers=[3.14,4,10,17,27,64,]
movies=["Brother Bear","The Lego Movie","Pokemon Ranger and the Temple of the Sea"]
combo=[foods[0],foods[5],numbers[1],numbers[4],movies[0],movies[1]]

print("Favorite foods:", foods)
print("Favorite numbers:", numbers)
print("Favorite movies:", movies)
print("Combo List:", combo)

print("Last food item=",foods[-1])
print("2nd, 4th and 6th numbers=",numbers[1],numbers[3],numbers[5])
print("All movies=",movies[0],movies[1],movies[2])
print("First food, first number and first movie=",foods[0],numbers[0],movies[0])

print("----------------Hands on 2----------------")
movies.append("The SpongeBob Squarepants Movie")
numbers.insert(3,3)
foods.insert(5,"Eggs and Toast Soldiers")

print("Added movie:", movies)
print("Added number at sub 3:", numbers)
print("Added food at sub 5:", foods)

del foods[6]
print("Deleted food[6]:", foods)
numbers.pop()
print("Deleted last number", numbers)
numbers.pop(2)
print("Deleted number at sub 2:", numbers)

print("----------------Hands on 3----------------")
movies.sort()
print("Sorted list:", movies)
foods.sort()
print("Sorted list:", foods)
print(sorted(numbers))
print(numbers)
movies.reverse()
print(movies)

print("---------------Chapter 4, Hands on 1---------------")
print("Food List\n--------------")
for food in foods: {
    print(food)
}

print("Number List\n--------------")
for number in numbers: {
    print(number)
}

print("Movie List\n--------------")
for movie in movies: {
    print(movie)
}

print("Combo List\n--------------")
for i in combo: {
    print(i)
}