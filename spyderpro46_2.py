class User:
    def __init__(self,name,username,email):
        self.name=name
        self.uname=username
        self.email=email
    def get_info(self):
        return f"username: {self.uname} name: {self.name} user email:{self.email}"