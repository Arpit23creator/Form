class Car:
    total_car = 0

    def __init__(self, brand, model, ):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1 

    def get_brand(self):
        return self.__brand + "!"

    def full_Name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_car = Car("Tata", "Safari")
# my_car.model = "City"
print(my_car.model)
# print(my_car.fuel_type())

# print(my_car.general_description())

# print(Car.general_description())


# my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
# print(my_tesla.fuel_type())

# print(Car.total_car)




# print(my_tesla.get_brand())



#print(my_tesla.__brand)

# print(my_tesla.full_Name())


# my_Car = Car("Toyota", "Corolla")
# print(my_Car.brand)
# print(my_Car.model)

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)
# print(my_new_car.full_Name())

