class auto:
    def __init__(self,model,color,carobe,price):
        self.model=model
        self.color=color 
        self.carobe=carobe 
        self.price=price 
        self.kilometer=0
    def get_info(self):
        return f"Model: {self.model},color: {self.calor}, carobe:{self.carobe}, price: {self.price}, length of driving:{self.kilometer}"
    def get_model(self):
        return self.model
    def get_color(self):
        return self.color
    def get_carobe(slef):
        return self.carobe
    def get_kilometer(self):
        return self.kilometer 
    def update_km(self):
        self.kilometer+=100
        