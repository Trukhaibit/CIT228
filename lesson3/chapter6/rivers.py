rivers={
    "Nile":"Egypt",
    "Mississippi":"The United States",
    "Congo":["Angola","Republic of the Congo","Democratic Republic of the Congo"]
}
print("--------------Rivers & Countries--------------")
for r in rivers:
    if type(rivers[r])==list:
        print(f"The {r} river runs through:")
        for i in rivers[r]:
                print("\t\t\t\t"+i)
    else:
        print(f"The {r} river runs through {rivers[r]}")
print("--------------Rivers--------------")
for r in rivers:
    print(r)
print("--------------Countries--------------")
for r in rivers:
    if type(rivers[r])==list:
        for i in rivers[r]:
                print(i)
    else:
        print(rivers[r])