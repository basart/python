from game.money_player.money_player import MoneyPlayer
import json


class Player(MoneyPlayer):
    def __init__(self, nick, login, password):
        MoneyPlayer.__init__()
        self.nick = nick
        self.login = login
        self.password = password

    def as_dict(self):
        d = {
            "type": self.__class__.__name__,
            "login": self.login
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.login = object_as_dict["login"]
        self.password = object_as_dict["password"]
        return object_as_dict

    def __str__(self):
        return '{}(login="{}")'.format(self.__class__.__name__, self.login)

if __name__ == "__main__":
    player1 = Player("vasgen", "vasya@mail.ru", "1111")
    print(player1.__str__())
    print(player1.total_number_of_gold)
    player1.silver_to_gold(100)
    print(player1.total_number_of_gold)
