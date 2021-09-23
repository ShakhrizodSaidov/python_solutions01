class Student:
    def __init__(self,name,surname,born):
        self.name = name
        self.surname=surname
        self.born=born
    def get_know(self):
        print(f"{self.name} {self.surname} was born in {self.born}")

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.name
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.lastname
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.name} {self.surname}"
    
    def tanishtir(self):
        print(f"Ismim {self.name} {self.surname}. {self.born} yilda tu'gilganman")
student1 = Student("Olim","Mavlonov",1998)
student2=Student('Shahrizod','Saidov',1999)
student3=Student('Xurshid','Dushanov',2000)