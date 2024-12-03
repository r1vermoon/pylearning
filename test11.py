#类
class Dog():
    def __init__(self,name,age) :
        self.name=name
        self.age=age
        self.location='China'

    def sit(self):
        print(self.name.title()+" is sitting now.")

    def roll_over(self):
        print(self.name.title()+" rolled over.")

my_dog=Dog('caicai',1)
my_dog.roll_over()
my_dog.location='Shandong'
print(my_dog.location)
print(my_dog.name.title())


#实例用作属性
class Battery():
    def __init__(self,battery=70) :
        self.battery=battery

    def descirbe_battery(self):
        print(self.battery)


#继承
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def get_descibe_name(self):
        print(str(self.year) + ' ' +self.make + ' ' + self.model)
    

class EleCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery()



my_car=EleCar('tesla','model s',2016)
my_car.get_descibe_name()
my_car.battery.descirbe_battery()

