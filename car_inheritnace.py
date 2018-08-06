class Car():
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        long_name=str(self.year)+ ' '+self.make+' '+self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't rollback odometer.")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
    def fill_gas_tank(self,fuel):
        self.gas_tank_capacity=fuel
        print("The gas tank is filled with "+str(self.gas_tank_capacity))

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    
    def describe_battery(self):
        print("This car has "+str(self.battery_size)+" kwh battery.")
    

class ElectricCar(Car):
    def __init__(self,make,model,year,battery_size):
        super().__init__(make,model,year)
        self.battery=Battery()
    
    
    # method overriding
    def fill_gas_tank(self):
            self.gas_tank_capacity=None
            print("Electric car doesn't have gas tank!!!")

