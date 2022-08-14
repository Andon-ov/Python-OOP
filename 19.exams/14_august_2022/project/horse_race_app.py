from project.factory import Factory


class HorseRaceApp:
    def __init__(self):
        self.horses: list = []
        self.jockeys: list = []
        self.horse_races: list = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if any([x.name == horse_name for x in self.horses]):
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = Factory.create_horse(horse_type, horse_name, horse_speed)
        if horse is not None:
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any([x.name == jockey_name for x in self.jockeys]):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Factory.create_jockey(jockey_name, age)
        if jockey is not None:
            self.jockeys.append(jockey)
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any([x.race_type == race_type for x in self.horse_races]):
            raise Exception(f"Race {race_type} has been already created!")

        race = Factory.create_race(race_type)
        if race is not None:
            self.horse_races.append(race)
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__hound_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self.__hound_horse_by_type(horse_type)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        # if not any([x.race_type == race_type for x in self.horse_races]):

        race = self.__found_race_by_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.__hound_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if any([x.name == jockey_name for x in race.jockeys]):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):

        race = self.__found_race_by_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        winner = sorted([x for x in race.jockeys], key=lambda x: -x.horse.speed)[0]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    def __hound_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None

    def __hound_horse_by_type(self, horse_type):
        for idx in range(len(self.horses) - 1, -1, -1):
            if self.horses[idx].__class__.__name__ == horse_type:
                if self.horses[idx].is_taken is False:
                    return self.horses[idx]
        return None

    def __found_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None
