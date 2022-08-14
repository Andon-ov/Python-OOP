from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class Factory:
    @staticmethod
    def create_horse(horse_type: str, horse_name: str, horse_speed: int):
        valid_horse_types = {"Appaloosa": Appaloosa,
                             "Thoroughbred": Thoroughbred}

        if horse_type in valid_horse_types:
            horse = valid_horse_types[horse_type](horse_name, horse_speed)

            return horse

    @staticmethod
    def create_jockey(jockey_name: str, age: int):
        jockey = Jockey(jockey_name, age)
        return jockey

    @staticmethod
    # dali ne trqbwa da prowerqwam za type
    def create_race(race_type):
        race = HorseRace(race_type)
        return race
