class Privileges:
    def __init__(self):
        self.privileges = ["can delete posts","can add posts","can ban users","can unban users"]
        
    def show_privileges(self):
        for p in self.privileges:
            print(p)