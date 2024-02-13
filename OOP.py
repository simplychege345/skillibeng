class Car:

    def __init__(self,make,model,year,colour):
        self.make=make
        self.model=model
        self.year=year
        self.colour=colour
    def onyesha(self):
        print(f"My dream car is  {self.make} and my model is {self.model} manufactured in {self.year} and colour is {self.colour}")
myobj=Car( "Toyota", "vits", "2020","black")

myobj.onyesha()
myobj2=Car("Telsa","vits","2045","white")
myobj2.onyesha()
