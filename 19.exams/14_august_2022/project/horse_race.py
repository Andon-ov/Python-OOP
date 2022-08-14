from project.validator import Validator


class HorseRace:
    def __init__(self,race_type: str):
        self.race_type = race_type
        self.jockeys: list = []
    #     An empty list that will store all the jockeys (objects) who will take part in the race.


    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        Validator.raise_error_when_have_invalid_race_type(value,"Race type does not exist!")
        self.__race_type = value