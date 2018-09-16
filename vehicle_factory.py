class Vehicle:
    
    _count_by_type = {2: 0, 3: 0, 4: 0}
    _max_speed = 0
    _model_name = ""

    def __init__(self, wheels, model, max_speed):
        self.wheels = wheels
        self._model_name = model
        self.current_speed = 0
        self._max_speed = max_speed
        self._count_by_type[wheels] += 1

    def get_model(self):
        print("Model of this {} wheeler is {}".format(self.wheels, self._model_name))

    def start(self):
        self.current_speed = self.default_initial_speed

    def move(self, speed):
        self.current_speed = speed

    def increase_speed_by(self, speed):
        self.current_speed += speed
    
    def set_max_speed(self, new_max_speed):
        self.max_speed = new_max_speed

    def get_max_speed(self):
        print("Max speed of {} wheeler: {} km/hr".format(self.wheels, self._max_speed))

    def apply_break(self):
        self.current_speed = 0

    def count_vehicles(self):
        return self._count_by_type[self.wheels]

    def total_all_vehicles(self):
        return sum(count for count in self._count_by_type.values())    

    
class TwoWheelerVehicle(Vehicle):
    
    def __init__(self, model):
        self.default_initial_speed = 20
        super().__init__(2, model, 40)  # for two wheeler vehicle

    # If all two wheelers move with the double speed than given speed
    def move(self, speed):
        self.current_speed += (speed*2)

    def apply_break(self):
        super()
        print("Break applied to two wheeler")


class ThreeWheelerVehicle(Vehicle):

    def __init__(self, model):
        self.default_initial_speed = 20
        super().__init__(3, model, 50)  # for three wheeler vehicle

    # If all three wheelers move with the tripple speed than given speed
    def move(self, speed):
        super().move(speed*3)
    
    def apply_break(self):
        super()
        print("Break applied to three wheeler")

            
class FourWheelerVehicle(Vehicle):

    def __init__(self, model):
        self.default_initial_speed = 20
        super().__init__(4, model, 60)  # for four wheeler vehicle

    # If all four wheelers move with the four times speed than given speed
    def move(self, speed):
        super().move(speed*4)

    def apply_break(self):
        super()
        print("Break applied to four wheeler")

    
if __name__ == '__main__':

    v2 = TwoWheelerVehicle("Bajaj")
    v3 = ThreeWheelerVehicle("Auto")
    v4 = FourWheelerVehicle("Hyhundi")

    v2.get_model()

    v2.start()
    print(v2.default_initial_speed)
    
    print(v2.current_speed)
    
    v2.set_max_speed(30)
    print(v2.get_max_speed())

    v2.move(2)
    print(v2.current_speed)

    v2.increase_speed_by(10)
    print(v2.current_speed)

    v2.apply_break()
    print(v2.current_speed)

    print(v2.count_vehicles())
    print(v2.total_all_vehicles())

    