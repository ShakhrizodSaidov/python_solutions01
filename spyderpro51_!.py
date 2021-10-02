class Auto:
    __num_auto=0
    def __init__(self,make,model,color,date,price):
        self.make=make
        self.model=model
        self.color=color
        self.date=date
        self.price=price
        Auto.__num_auto+=1
    def __repr__(self):
        return f"auto:{self.model}"

class autosalon:
    counter=0
    def __init__(self,name):
        self.name=name
        self.autos=[]
    def __repr__(self):
        return f"autosalon:{self.name}"
    
    def add_auto(self,auto):
        return self.autos.append(auto)
    def get_auto(self,auto):
        return f"{self.autos}"
        
    
salon1=autosalon("EUROAUTOs")
# auto obyektlarini yaratamiz
auto1 = Auto("GM","Malibu","Qora",2020,40000)
auto2 = Auto("GM","Lacetti","Oq",2020,20000)
auto3 = Auto("Toyota",'Carolla',"Silver",2018, 45000)

# Yuqoridagi obyektlarni salon1 ga qo'shamiz
for auto in [auto1, auto2, auto3]: 
    salon1.add_auto(auto)