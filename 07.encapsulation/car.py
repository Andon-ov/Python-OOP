class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def drive(self):
        print(f'driving max speed {str(self.max_speed)}')

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        self.__max_speed = min(value, 447)


red_car = Car(200)
red_car.drive()
red_car.max_speed = 512

