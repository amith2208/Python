class Car:
    
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
        
    def details(self):
        print("Car brand "+self.name+" color is "+self.color+" price "+self.price)

while(True):
    print("1. Retry")
    print("2. Exit")
    print("Enter the choice")
    c=int(input())
    if c==1:
        name=input("Enter name of car: ")
        color=input("Enter the car color: ")
        price=input("Enter the price: ")
        NewCar=Car(name,color,price)
        NewCar.details()
    elif c==2:
        exit()
    else:
        print("Enter correct choice")
        
