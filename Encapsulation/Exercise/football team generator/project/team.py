from project.player import Player


class Team:
    def __init__(self, name:str, rating:int):
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []

    def add_player(self, player:Player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name:str):
        current_player = next((pl for pl in self.__players if pl.name == player_name), None)
        if current_player is not None:
            self.__players.remove(current_player)
            return current_player
        return f"Player {player_name} not found"


