class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):

        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if not player.guild == self.name and not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def guild_info(self):
        data = f"Guild: {self.name}\n"
        for player in self.players:
            data += player.player_info()
            return data

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."
