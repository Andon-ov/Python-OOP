from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: list = []
        self.supplies: list = []

    def add_player(self, *player: Player):
        player_name = []

        for pl in player:
            if pl not in self.players:
                self.players.append(pl)
                player_name.append(pl.name)

        return f"Successfully added: {', '.join([x for x in player_name])}"

    def add_supply(self, *supply: Supply):
        for sp in supply:
            self.supplies.append(sp)

    def sustain(self, player_name: str, sustenance_type: str):
        supply_type = {"Food": Food,
                       "Drink": Drink}
        player = self.found_player_by_name(player_name)
        if player is None:
            return
        if sustenance_type not in supply_type:
            return
        supply, index = self.found_supply_by_type(sustenance_type)

        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if player.need_sustenance is False:
            return f"{player_name} have enough stamina."

        player.stamina = min(player.stamina + supply.energy, 100)
        self.supplies.pop(index)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):

        first_player = self.found_player_by_name(first_player_name)
        second_player = self.found_player_by_name(second_player_name)

        result = self.any_player_have_low_stamina(first_player, second_player)
        if result:
            return result

        player_one, player_two = sorted([first_player, second_player], key=lambda x: x.stamina)

        player_two.stamina = max(player_two.stamina - (player_one.stamina / 2), 0)
        if player_two.stamina == 0:
            return f"Winner: {player_one.name}"
        player_one.stamina = max(player_one.stamina - (player_two.stamina / 2), 0)
        if player_one.stamina == 0:
            return f"Winner: {player_two.name}"

        winner = sorted([first_player, second_player], key=lambda x: -x.stamina)[0]
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - (player.age * 2), 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ''
        for player in self.players:
            result += str(player) + '\n'
        for supply in self.supplies:
            result += supply.details() + '\n'

        return result.strip()

    def found_supply_by_type(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[idx].__class__.__name__ == sustenance_type:
                return self.supplies[idx], idx
        return None, -1

    def found_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return None

    @staticmethod
    def any_player_have_low_stamina(first_player, second_player):
        return_result = ''
        if first_player.stamina == 0:
            return_result += f"Player {first_player.name} does not have enough stamina.\n"
        if second_player.stamina == 0:
            return_result += f"Player {second_player.name} does not have enough stamina."
        return return_result.strip()
