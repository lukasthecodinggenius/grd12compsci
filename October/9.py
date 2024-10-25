#Using inheritance in object-oriented programming allows for better code reusability and organization by reduing repetitiveness


class Appliance:
    def __init__(self, brand):
        self.brand = brand
        
    def turn_on(self):
        print(f"{self.brand} appliance is now on.")

class WashingMachine(Appliance):
    def wash_clothes(self):
        print(f"{self.brand} washing machine is washing clothes.")

class Refrigerator(Appliance):
    def cool_food(self):
        print(f"{self.brand} refrigerator is cooling food.")

washer = WashingMachine("LG")
fridge = Refrigerator("Samsung")

washer.turn_on()       
washer.wash_clothes()  
fridge.turn_on()       
fridge.cool_food()     
