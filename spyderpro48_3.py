class Shaxs:
    def __init__(self,name,surname,passport,born):
        self.name = name
        self.surname = surname
        self.passport = passport
        self.born = born
    
    def get_info(self):
        info = f"{self.name} {self.surname}. "
        info += f"Passport:{self.passport} was born {self.born}"
        return info
        
    def get_age(self,yil):
        return yil - self.born
class Manzil:
    def __init__(self,home,street,subregion,region):
        self.home = home
        self.street = street
        self.subregion = subregion
        self.region = region
    
    def get_manzil(self):
        manzil = f"{self.region} regioni, {self.subregion} subregioni, "
        manzil += f"{self.street} ko'chasi, {self.home}-home"
        return manzil
class Talaba(Shaxs):
    __counter=0
    def __init__(self,name,surname,passport,born,idraqam):
        super().__init__(name, surname, passport, born)
        self.idraqam = idraqam
        self.bosqich = 1
        Talaba.__counter+=1
    
    def get_id(self):
        return self.idraqam
    
    def get_course(self):
        return self.bosqich