from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

        # Private attribute players: list - empty list upon initialization that will contain all the players (objects)

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for p in self.__players:
            if p.name == player_name:
                result = p
                self.__players.remove(p)
                return result
        return f"Player {player_name} not found"
        # oRemove the player and return him
        # oIf the player is not in the team, return "Player {player_name} not found"

# from project.player import Player
#
#
# class Team:
#     def __init__(self, name, rating):
#         self.__players = []
#         self.__rating = rating
#         self.__name = name
#
#     def add_player(self, player: Player):
#         for team_player in self.__players:
#             if player.name == team_player.name:
#                 return f"Player {player.name} has already joined"
#
#         self.__players.append(player)
#         return f"Player {player.name} joined team {self.__name}"
#
#     def remove_player(self, player_name:str):
#         for team_player in self.__players:
#             if team_player.name == player_name:
#                 self.__players.remove(team_player)
#                 return team_player
#         return f"Player {player_name} not found"
