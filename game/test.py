from player import Player
from moderator import Moderator
from administrator import Administrator
from game_session import GameSession
from money_player import MoneyPlayer
from player_achievements import PlayerAchievements
from counters_player import CountersPlayer

if __name__ == '__main__':
    player_vasya = Player(1, "vasilij", "vasya@mail.ru", "1435223")
    player_boris = Player(2, "boris", "boris@mail.ru", "1223")
    player_akakij = Player(3, "akakij", "akakij@mail.ru", "13435")
    player_vasya.save_to_db()
    player_boris.save_to_db()
    player_akakij.save_to_db()
    player = Player(1)
    player.load_from_db('vasya@mail.ru')
    print(player)
    print('player={}, money={}, counters={}'.format(player.name, player.get_money_player(), player.get_counters_player()))

    counetrs_player_1 = CountersPlayer(1, 4030, 1212, 15)
    counetrs_player_2 = CountersPlayer(2, 400, 12, 5)
    counetrs_player_3 = CountersPlayer(3, 10000, 1222, 6)
    counetrs_player_1.save_to_db()
    counetrs_player_2.save_to_db()
    counetrs_player_3.save_to_db()

    achievements_player_1 = PlayerAchievements(1, 1)
    achievements_player_2 = PlayerAchievements(2, 4)
    achievements_player_3 = PlayerAchievements(3, 4)
    achievements_player_1.save_to_db()
    achievements_player_2.save_to_db()
    achievements_player_3.save_to_db()

    money_player_1 = MoneyPlayer(1)
    money_player_2 = MoneyPlayer(2)
    money_player_3 = MoneyPlayer(3)
    money_player_1.save_to_db()
    money_player_2.save_to_db()
    money_player_3.save_to_db()


    player1 = Player(1)
    player1.load_from_db('vasya@mail.ru')
    print(player1)
    print('player={}, money={}, counters={}'.format(player1.name, player1.get_money_player(), player1.get_counters_player()))

    player2 = Player(2)
    player2.load_from_db('boris@mail.ru')
    print(player2)
    print('player={}, money={}, counters={}'.format(player2.name, player1.get_money_player(), player2.get_counters_player()))

    player3 = Player(3)
    player3.load_from_db('akakij@mail.ru')
    print(player3)
    print('player={}, money={}, counters={}'.format(player3.name, player3.get_money_player(), player3.get_counters_player()))



