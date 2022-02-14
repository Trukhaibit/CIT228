from user import User
from privileges import Privileges
from admin import Admin

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
