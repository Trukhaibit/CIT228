from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self,first_name,last_name,join_date,birth_date,followers):
        super().__init__(first_name,last_name,join_date,birth_date,followers)
        self.privileges = Privileges()