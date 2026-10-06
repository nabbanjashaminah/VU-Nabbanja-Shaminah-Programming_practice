#Conditionals
age = 25
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")


#loops
number = 4
for i in range(0, number):
    print(i)


#Classes
class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

car = Car()
print(car.make)
print(car.model)
print(car.year)

    








    