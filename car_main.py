from car_inheritnace import ElectricCar
from car_inheritnace import Car as C

mytesla=ElectricCar('tesla','model S',2016,70)
print(mytesla.get_descriptive_name())

mytesla.fill_gas_tank()
print(mytesla.gas_tank_capacity)
mytesla.battery.describe_battery()
mytesla.battery.battery_size=100
mytesla.battery.describe_battery()