class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sefa = "xxw"

    def sit(self):
        print(str(self.name).title() +" is now sitting")

    def roll_over(self):
        print(str(self.name).title() +" is rolling over")

    def updatesefa(self):
        self.sefa = 2

my_dog = Dog('selina',6)
print(my_dog.name)
my_dog.sit()
my_dog.roll_over()
my_dog.sefa = 1
my_dog.updatesefa()
print(my_dog.sefa)

class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
       long_name = str(self.year) + ' ' + self.make + ' ' + self.model
       return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.odometer_reading = 0
        self.battery_size = 70

    def increment_odometer(self,miles):
        self.odometer_reading = miles


my_tesla = ElectricCar('tesla','model-s',2020)
print(my_tesla.get_descriptive_name())
print(my_tesla.battery_size)
my_car = Car('moto','V&',2019)
my_car.increment_odometer(10)

my_tesla.increment_odometer(500)
print(str(my_car.odometer_reading) +"----"+str(my_tesla.odometer_reading))

filename = 'programming.txt'

with open(filename,'a') as file_object:
    file_object.write("i love python\n")
    file_object.write("i love u ")
