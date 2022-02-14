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