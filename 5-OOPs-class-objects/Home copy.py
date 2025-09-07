class Home():
    def __init__(self,size,location,builder_name,price):
        self.size = size
        self.location = location
        self.builder_name = builder_name
        self.price = price
        self.flats = 100
    
    def buy_house(self,customer_name):
        print(customer_name," you have bought a house in", self.location," for ",self.price," of size ",self.size," built by ",self.builder_name)
        self.flats -= 1
        print("Flats left:", self.flats)


manager1=Home("3BHK","Bangalore","ABC Builders",5000000)
manager1.buy_house("Amit")
manager2=Home("2BHK","Chennai","XYZ Builders",3000000)  

manager2.buy_house("Rakesh")
manager2.buy_house("Suresh")
manager2.buy_house("John")
manager2.buy_house("Smith")
