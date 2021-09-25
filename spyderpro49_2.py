class User():
    def __init__(self,name,surname,passport,born,phone):
        self.name=name
        self.surname=surname
        self.passport=passport
        self.born=born
        self.phone=phone 
    def get_info(self):
        info=f"Name: {self.name}\nsurname:{self.surname}\npassport: {self.passport}"
        info+=f"Year of born: {self.born}\nphone nuber: {self.born}"
        return info        
class Admin(User):
    def __init__(self,name,surname,login,parol):
        super().__init__(self,name,surname)
        self.login=login
        self.parol=parol
    def ban_user(self):
        return f"user has blocked!"