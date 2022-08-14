from project.factory import Factory


class HorseRaceApp:
    def __init__(self):
        self.horses: list = []
        self.jockeys: list = []
        self.horse_races: list = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if any(x.name == horse_name for x in self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = Factory.create_horse(horse_type,horse_name,horse_speed)
        if horse is not None:
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any(x.name == jockey_name for x in self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Factory.create_jockey(jockey_name,age)
        if jockey is not None:
            self.jockeys.append(jockey)
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(x.race_type == race_type for x in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")

        race = Factory.create_race(race_type)
        # The method creates a race and adds it to the horse races' list.
        #     • When it is successfully created and added, the method returns the message "Race {race_type} is created."


    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        pass
        # Sets the last horse added from the given horse type to the jockey with the given name (if they both exist).
        #     • If the jockey does NOT exist in the jockeys' list, raise an Exception with the message "Jockey {jockey_name} could not be found!"
        #     • If there is no available horse (all horses of that type are taken, or no horse of that type exists) of the given type in the horses' list, raise an Exception with the message "Horse breed {horse_type} could not be found!".
        #     • If there is an available horse (the horse is not taken), but the jockey already has a horse, return the message: "Jockey {jockey_name} already has a horse."
        #     • If the horse can be added to the jockey, take it, and set it to the jockey. Then, return the message: "Jockey {jockey_name} will ride the horse {horse_name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        pass
        # Adds a jockey (object) to the given horse race type (if they both exist). A jockey can only participate in a horse race if he has a horse.
        #     • If a horse race of that type does NOT exist in the list with horse races, raise an Exception with the message "Race {race_type} could not be found!"
        #     • If the jockey does NOT exist in the jockeys' list, raise an Exception with the message "Jockey {jockey_name} could not be found!"
        #     • If the jockey is on the jockeys' list, but he/she doesn't have a horse, raise an Exception with the message "Jockey {jockey_name} cannot race without a horse!"
        #     • If the jockey has already been added to the horse race, return the message "Jockey {jockey_name} has been already added to the {race_type} race."
        #     • If both the race type and the jockey exist and the jockey has a horse, add the jockey (object) to the given horse race and return the message: "Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        pass
        #     • If the horse race does NOT exist, raise an Exception with the message "Race {race_type} could not be found!"
        #     • The participants in a horse race must be at least 2. Otherwise, raise an Exception with the message "Horse race {race_type} needs at least two participants!"
        #     • If the race can be started, you should choose the winner - he/she is the jockey who rode the horse with the highest speed. Note: there will NOT be two or more jockeys riding their horse at the same highest speed. In the end, return the message:
        # "The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_name}! Winner's horse: {horse_name}."
