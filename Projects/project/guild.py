from food.project import Player


class Guild:
    def __init__(self, name:str):
        self.name = name
        self.players = []

    def assign_player(self, player:Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != self.name and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name:str):
        pl = next((pl for pl in self.players if pl.name == player_name), None)
        if pl:
            self.players.remove(pl)
            pl.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = "\n".join(player.player_info() for player in self.players)
        return f"Guild: {self.name}\n{result}"

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
