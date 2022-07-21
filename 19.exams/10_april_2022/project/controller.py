from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: list = []
        # An empty list that will contain all the players (objects)
        self.supplies: list = []

        # An empty list that will contain all the supplies (objects)


    def add_player(self, *player: Player):
        pass

    # Add the players to the players' list. You should not add a player who has already been added.
    # In the end, return a message with the successfully added players' names, separated with a comma and a space (", ") in the format: "Successfully added: {name1}, {name2}, … {nameN}"

    def add_supply(self, *supply: Supply):
        pass

    # Add all supplies to the supplies list
    # A supply could be added multiple times

    def sustain(self, player_name: str, sustenance_type: str):
        pass

    # Use the last supply added from the given type to sustain the player (increase his stamina with the supply's energy value and remove the supply from the list) and return the message "{player_name} sustained successfully with {supply_name}."
    # A player always uses the whole amount (units) of the given supply, but his stamina cannot enhance above 100 (it should be set to 100).
    # If the player doesn't need sustenance, it won't be appropriate to waste a supply. Just return the message "{player_name} have enough stamina."
    # If the given type is food, but there is no food left, raise an Exception with the message "There are no food supplies left!"
    # If the given type is drink, but there are no drinks left, raise an Exception with the message "There are no drink supplies left!"
    # The valid sustenance types are "Food" and "Drink". In any other case, ignore the command.
    # If the player is not in the players list, ignore the command.

    def duel(self, first_player_name: str, second_player_name: str):
        pass

    # The two players participate in a duel, each of them could only attack once.
    # If a player's stamina is 0, he could not participate in a duel. In that case, return a message "Player {player_name} does not have enough stamina." and discontinue the duel. If both players' stamina is 0, return the message for both players on separate lines, starting from the first one given.
    # If both players have a positive value of stamina, the duel begins:
    # oThe player with a lower value of stamina attacks first. He reduces the other player's stamina by a value equal to one-half of his own (the attacker's) stamina.
    # oNext, the other player attacks the same way (reduces the first player's stamina by a value equal to one-half of his own (the second attacker's) stamina).
    # oIf, during the duel, a player's stamina becomes equal to or less than 0, it should be set to 0. The player immediately loses the duel, and the other player becomes a winner.
    # oOtherwise, the winner is the player who has left with more stamina.
    # oReturn the winner's name in the format: "Winner: {winner_name}"
    # Note: there will be no case where both players will have equal stamina values at the beginning or in the end.
    # Note: the players will always exist in the players list.

    def next_day(self):
        pass

    # First, the stamina of each added player gets reduced by the result of multiplying their age by 2
    # If a player's stamina becomes less than 0, it should be set to 0
    # Then, you need to sustain each player by giving them one food (first) and one drink (second)

    def __str__(self):
        pass
    # Override the method so that its return the players' data and the supplies' data in the format:
    # "Player: {player_name_1}, {age}, {stamina}, {need_sustenance}
    # Player: {player_name_2}, {age}, {stamina}, {need_sustenance}
    # ...
    # Player: {player_name_N}, {age}, {stamina}, {need_sustenance}
    # {supply_type}: {name_1}, {energy}
    # {supply_type}: {name_2}, {energy}
    # ...
    # {supply_type}: {name_N}, {energy}"
