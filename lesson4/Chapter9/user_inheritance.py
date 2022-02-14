class User:
    def __init__(self,first_name,last_name,join_date,birth_date,followers):
        self.first_name = first_name
        self.last_name = last_name
        self.join_date = join_date
        self.birth_date = birth_date
        self.followers = followers
        self.login_attempts = 0

    def describe_user(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Join date:", self.join_date)
        print("Birth date:", self.birth_date)
        print("Followers:", self.followers)

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.first_name} has attempted to log in {self.login_attempts} times.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login attempts reset for", self.first_name)
class Privileges:
    def __init__(self):
        self.privileges = ["can delete posts","can add posts","can ban users","can unban users"]
        
    def show_privileges(self):
        for p in self.privileges:
            print(p)
 
class Admin(User):
    def __init__(self,first_name,last_name,join_date,birth_date,followers):
        super().__init__(first_name,last_name,join_date,birth_date,followers)
        self.privileges = Privileges()

admin = Admin("Johnathan","Kowak","2/13/2022","2/13/2002","38")
user2 = User("Nathan","Gacharach","1/12/2021","11/11/2001","708")
user3 = User("Timothy","Kowalski","5/7/1998","11/11/1980","12708")
user9_5 = User("Natalie","Shrock","2/2/2021","2/3/2008",10)

print("----------Excercise 9-3----------")
admin.greet_user()
admin.describe_user()
user2.greet_user()
user2.describe_user()
user3.greet_user()
user3.describe_user()

print("----------Excercise 9-5----------")
user9_5.increment_login_attempts()
user9_5.increment_login_attempts()
user9_5.increment_login_attempts()
user9_5.increment_login_attempts()
user9_5.increment_login_attempts()
user9_5.increment_login_attempts()
user9_5.greet_user()
user9_5.reset_login_attempts()
print(user9_5.login_attempts)

print("----------Excercise 9-7 and 9-8----------")
admin.privileges.show_privileges()

