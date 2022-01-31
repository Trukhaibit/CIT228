fruit1 = "Mangosteen"
fruit2 = "Mango"
num1 = 7
num2 = 10
direction1 = "north"
direction2 = "northeast"
cardinals=["north","east","west","south"]

print("========== True Results ==========")
print(f"{num1} < {num2}:", num1 < num2)
print(f"{num1} <= {num2}:", num1 <= num2)
print(f"{num1} == {num1}:", num1 == num1)
print(f"{fruit1} == {fruit1}:", fruit1 == fruit1)
print(f"{fruit1} != {fruit2}:", fruit1 != fruit2)
print(f"{fruit1} != {fruit1.lower()}:", fruit1 != fruit1.lower())
print(f"{fruit1} != {fruit2} and {fruit1} != {fruit1.lower()}:", fruit1 != fruit2 and fruit1 != fruit1.lower())
print(f"{fruit1} == {fruit1} or {fruit1} == {fruit2}:", fruit1 == fruit1 or fruit1 == fruit2)
print(f"{direction1} in cardinals:", direction1 in cardinals,)
print(f"{direction2} not in cardinals:", direction2 not in cardinals,)
print("========== False Results ==========")
print(f"{num1} > {num2}:", num1 > num2)
print(f"{num1} >= {num2}:", num1 >= num2)
print(f"{num1} == {num2}:", num1 == num2)
print(f"{fruit1} != {fruit1}:", fruit1 != fruit1)
print(f"{fruit1} == {fruit2}:", fruit1 == fruit2)
print(f"{fruit1} == {fruit1.lower()}:", fruit1 == fruit1.lower())
print(f"{fruit1} != {fruit2} and {fruit1} == {fruit1.lower()}:", fruit1 != fruit2 and fruit1 == fruit1.lower())
print(f"{fruit1} != {fruit1} or {fruit1} == {fruit2}:", fruit1 != fruit1 or fruit1 == fruit2)
print(f"{direction1} not in cardinals:", direction1 not in cardinals,)
print(f"{direction2} in cardinals:", direction2 in cardinals,)