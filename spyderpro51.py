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
        return f"Make:{self.make}\nModel:{self.model} \nColor:{self.color} \nDate:{self.date} \nYear:{self.date} \nPrice:{self.price}"
    def __eq__(self, another_auto):
        return self.price==another_auto.price
    def __le__(self, another_auto):
        return self.price<=another_auto.price
    def __ge__(self, another_auto):
        return self.price>=another_auto.price
    def __lt__(self, another_auto):
        return self.price<another_auto.price
  
    def __gt__(self, another_auto):
        return self.price>another_auto.price
    def __ne__(self, another_auto):
        return self.price!=another_auto.price
      
      
      
    
# # print(auto1,"\n\n",auto2)

auto1 = Auto("GM","Malibu","Black",2020,40000)
auto2 = Auto("GM","Lacetti","White",2020,20000)