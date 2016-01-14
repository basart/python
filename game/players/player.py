import json
import game.money_player.money_player as mp


class Player(mp.MoneyPlayer):
    def __init__(self, nick=None, login=None, password=None):
        mp.MoneyPlayer.__init__(self)
        self.nick = nick
        self.login = login
        self.password = password

    def as_dict(self):
        d = {
            'type': self.__class__.__name__,
            'nick': self.nick,
            'login': self.login,
            'password': self.password,
            'bag': {'gold': self.total_number_of_gold, 'silver': self.total_number_of_silver}
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.nick = object_as_dict['nick']
        self.login = object_as_dict['login']
        self.password = object_as_dict['password']
        self.total_number_of_silver = object_as_dict['bag']['silver']
        self.total_number_of_gold = object_as_dict['bag']['gold']
        return object_as_dict

    def __str__(self):
        return '{}(nick="{}", login="{}", password="{}", gold={}, silver={})'.format(
            self.__class__.__name__,
            self.nick,
            self.login,
            self.password,
            self.total_number_of_gold,
            self.total_number_of_silver
        )

if __name__ == "__main__":
    # player1 = Player("vasgen", "vasya@mail.ru", "1111")
    # print(player1.__str__())
    # print(player1.total_number_of_gold)
    # player1.silver_to_gold(100)
    # player1.save(open('object_'+player1.login+'.txt', 'w'))
    # print(player1.total_number_of_gold)
    deserialized_player = Player()
    deserialized_player.load(open("object_vasya@mail.ru.txt"))
    print("deserialized player is {}".format(deserialized_player))
