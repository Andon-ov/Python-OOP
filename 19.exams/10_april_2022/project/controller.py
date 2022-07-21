from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: list = []
        # An empty list that will contain all the players (objects)
        self.supplies: list = []
        # An empty list that will contain all the supplies (objects)

    def add_player(self, *players: Player):
        result = []
        for player in players:
            if player not in self.players:
                result.append(player.name)
                self.players.append(player)
        return f"Successfully added: {', '.join([x for x in result])}"

        # Add the players to the players' list.
        # You should not add a player who has already been added.
        # In the end, return a message  (", ") in the format: "Successfully added: {name1}, {name2}, … {nameN}"

    def add_supply(self, *supplys: Supply):
        for supply in supplys:
            self.supplies.append(supply)

        # Add all supplies to the supplies list
        # A supply could be added multiple times

    def sustain(self, player_name: str, sustenance_type: str):
        food = sum([1 for x in self.supplies if x.__class__.__name__ == 'Food'])
        drink = sum([1 for x in self.supplies if x.__class__.__name__ == 'Drink'])

        # The valid sustenance types are "Food" and "Drink". In any other case, ignore the command.
        # If the player is not in the players list, ignore the command.

        player = self.found_player(player_name)
        if sustenance_type not in "Food""Drink":
            return
        if player is None:
            return
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        # If the player doesn't need sustenance, it won't be appropriate to waste a supply.
        # Just return the message "{player_name} have enough stamina."
        if sustenance_type == "Food" and food == 0:
            raise Exception("There are no food supplies left!")
        # If the given type is food, but there is no food left,
        # raise an Exception with the message

        if sustenance_type == "Drink" and drink == 0:
            raise Exception("There are no drink supplies left!")
        # If the given type is drink, but there are no drinks left,
        # raise an Exception with the message "There are no drink supplies left!"
        supply = self.supplies[::-1]
        sustenance = None
        for sp in supply:
            if sp.__class__.__name__ == sustenance_type:
                sustenance = sp
                break
        if player.stamina + sustenance.energy > 100:
            player.stamina = 100
        else:
            player.stamina += sustenance.energy
        self.supplies.remove(sustenance)
        return f"{player.name} sustained successfully with {sustenance.name}."


        # Use the last supply added from the given type to sustain the player
        # (increase his stamina with the supply's energy value and remove the supply from the list)
        # and return the message "{player_name} sustained successfully with {supply_name}."

        # A player always uses the whole amount (units) of the given supply,
        # but his stamina cannot enhance above 100 (it should be set to 100).

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
        result = ''
        for pl in self.players:
            result += str(pl)
            result += '\n'
        for sp in self.supplies:
            result += sp.details()
            result += '\n'
        return result.strip()

    def found_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return None
