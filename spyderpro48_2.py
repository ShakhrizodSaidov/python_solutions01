# # polimorfizm
# class Shaxs:
#     def __init__(self,name,surname,passport,born):
#         self.name = name
#         self.surname = surname
#         self.passport = passport
#         self.born = born
    
    def get_info(self):
        info = f"{self.name} {self.surname}. "
        info += f"Passport:{self.passport} was born {self.born}"
        return info
        
#     def get_age(self,yil):
#         return yil - self.born
# class Talaba(Shaxs):
#     def __init__(self,name,surname,passport,born,idraqam):
#         self.idraqam = idraqam
#         self.bosqich = 1
    
#     def get_id(self):
#         return self.idraqam
    
#     def get_course(self):
#         return self.bosqich
    
    def get_info(self):
        info = f"{self.name} {self.surname}. "
        info += f"{self.get_course()}-bosqich. ID raqami: {self.idraqam}"
        return info