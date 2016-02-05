from player import Player
from moderator import Moderator
from administrator import Administrator
from game_session import GameSession
from money_player import MoneyPlayer
from player_achievements import PlayerAchievements
from counters_player import CountersPlayer

if __name__ == '__main__':
    # player = Player(3, 'poc', 'poc@mail.ru', 'asdfsadf123')
    # counetrs_player = CountersPlayer(1, 1, 100, 344, 3)
    # counetrs_player.save_to_db()
    money_player = MoneyPlayer()
    money_player.load_from_db(1)
    # money_player.delete_from_db()
    print(money_player)
    # achievement_player = PlayerAchievements(2, 2, 2)
    # achievement_player.save_to_db()
    money_player = MoneyPlayer(1, 1, 'gold', 10000)
    # session_player = GameSession(1, 1)
    # session_player.delete_from_db()
    # session_player.save_to_db()

    money_player.save_to_db()
    # player.delete_from_db()
    # player1 = Player(2, 'chel', 'chel@mail.ru', 'sd9f7gs9d87f')
    # print(player)
    # print(player1)
    # player.save_to_db()
    # player1.save_to_db()

