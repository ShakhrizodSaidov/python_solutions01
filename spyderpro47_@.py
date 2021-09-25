class autosalon():
    def __init__(self,name,address,phone_number,email,website,cars):
        self.name = name
        self.address=address
        self.phone_number=phone_number
        self.email=email
        self.website=website
        self.cars=[]
    def add_cars(self):
        return [self.cars.append(x) for x in self.cars]
    def get_cars(self):
        return [car for car in  self.cars ]