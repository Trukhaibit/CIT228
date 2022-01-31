users=["Peter Griffin","Lois Griffin","Megatron Griffin","Christopher Griffin","Stuart Griffin","Brian Griffin"]
new_users=["Homer Simpson","Marjorie Simpson","Bartholomew Simpson","Stuart Griffin","Christopher Griffin"]
lower_users=[]
for user in users:
    lower_users.append(user.lower())

for user in new_users: 
    if user.lower() in lower_users:
        print(f"That name has already been taken, {user}, you will have to pick a new one.")
    else:
        print(f"The user name, {user}, is available")