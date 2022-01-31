users=["Peter Griffin","Lois Griffin","Megatron Griffin","Christopher Griffin","Stuart Griffin","Brian Griffin","admin"]
if users:
    for user in users:
        if user=="admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to get some users!")
