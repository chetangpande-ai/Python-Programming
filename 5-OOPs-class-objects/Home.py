class Home():
    def __init__(self):
        self.flats = 100
        self.location = "Bangalore"
        self.price = 5000000
    
    def buy_house(self,customer_name):
        print(customer_name," you have bought a house in", self.location," for ",self.price)
        self.flats -= 1
        print("Flats left:", self.flats)


buyer=Home()
buyer.buy_house("Amit")
buyer.buy_house("Rakesh")
buyer.buy_house("Suresh")
buyer.buy_house("John")
buyer.buy_house("Smith")
