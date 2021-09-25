class Shaxs():
    __counter=0
    def __init__(self,name,surname,passport,born,num_married):
        self.name = name
        self.surname = surname
        self.passport = passport
        self.born = born
        self.__num_married=num_married
        Shaxs.__counter+=1

    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    def update_married(self):
        self.__num_married+=1
        return self.__num_married

shaxs1 = Shaxs("Alijon","Valiyev","FA010101",2000,1)
shaxs2 = Shaxs("Hasan","Husanov","FB0011223",1998,2)            
    