class Car:
    #Setting a Default Value for an Attribute
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0 #->default value for a attribute
    
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    # Modifying an Attribute’s Value Through a Method
    def update_odo(self,mileage):
        self.odometer_reading=mileage

    
my_car=Car('mclaren','p1',2013)
print(my_car.get_descriptive_name())
my_car.read_odometer()

# Modyfying attributes value
my_car.odometer_reading=23
my_car.read_odometer()

my_car.update_odo(23)
my_car.read_odometer()


