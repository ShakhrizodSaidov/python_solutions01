class Person():
    __counter=0
    def __init__(self,name,surname,passport,born,num_married):
        self.name = name
        self.surname = surname
        self.passport = passport
        self.born = born
        self.__num_married=num_married
        Person.__counter+=1

    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    def update_married(self):
        self.__num_married+=1
        return self.__num_married


from spyderpro48_3 import Talaba

person1 = Talaba("Alijon","Valiyev","FA010101",2000,1)
person2= Talaba("Hasan","Husanov","FB0011223",1998,2)            