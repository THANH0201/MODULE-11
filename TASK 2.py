class Car:
    def __init__(self,reg_num, max_speed):
        self.registration_number = reg_num
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Change speed
    def accelerate(self,speed_change):
        self.current_speed = speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

#time drive
    def drive(self, time):
        self.travelled_distance += round((self.current_speed * time)) #(d=v.t)

class ElectricCar(Car):
    def __init__(self,reg_num,max_speed, battery_capacity):
        super().__init__(reg_num, max_speed)
        self.battery_capacity = battery_capacity

    def print_travelled_distance(self):
        print(f"The traveled distance of the electronic car {self.registration_number} is:{self.travelled_distance} km")

class GasCar(Car):
    def __init__(self,reg_num,max_speed, tank_capacity):
        super().__init__(reg_num, max_speed)
        self.tank_capacity = tank_capacity

    def print_travelled_distance(self):
        print(f"The traveled distance of the gas car {self.registration_number} is:{self.travelled_distance} km")

el_car1 = ElectricCar('ACD-01',180,60.5)
gas_car1= GasCar('ABC-01',170,35)
el_car1.accelerate(30.)
gas_car1.accelerate(100.)
el_car1.drive(3.)
gas_car1.drive(3.)
el_car1.print_travelled_distance()
gas_car1.print_travelled_distance()