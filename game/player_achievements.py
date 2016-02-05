import json
import datetime
import db
from counters_player import CountersPlayer


class PlayerAchievements(CountersPlayer):
    def __init__(self, id=None, player_id=None, achievement_id=0, created=None):
        self.id = id
        self.player_id = player_id
        self.achievement_id = achievement_id
        self.created = datetime.datetime.now()

    def as_dict(self):
        d = {
            "type": self.__class__.__name__,
            "id": self.id,
            "player_id": self.player_id,
            "achievement_id": self.achievement_id,
            "created": self.created
        }
        return d

    def save_to_db(self):
        cursor = db.connect.cursor()
        sql_data = self.as_dict()
        insert_query = 'insert into achievements (id, player_id, achievement_id, created)' \
            ' values (%(id)s, %(player_id)s, %(achievement_id)s, %(created)s'
        # update_query = 'update achievements ' \
        #     'set player_id=%(player_id)s, achievement_id=%(achievement_id)s, created=%(created)s' \
        #     'where id=%(id)s'
        try:
            cursor.execute(insert_query, sql_data)
        except db.IntegrityError:
            # cursor.execute(update_query, sql_data)
            print('Achievement already exists')
        db.connect.commit()

    def delete_from_db(self):
        cursor = db.connect.cursor()
        sql_data = {
            'id': self.id
        }
        query_for_delete_money = 'delete from achievements where id=%(id)s'
        try:
            cursor.execute(query_for_delete_money, sql_data)
        except db.IntegrityError:
            print('error delete money')

    def load_from_db(self, player_id):
        cursor = db.connect.cursor()
        sql_data = {
            'player_id': player_id
        }
        query_for_load_money = 'select * from achievements where player_id=%(player_id)s'
        try:
            cursor.execute(query_for_load_money, sql_data)
            db_row = cursor.fetchone()
            self.id = db_row[0]
            self.player_id = db_row[1]
            self.achievement_id = db_row[2]
            self.created = db_row[3]

        except db.IntegrityError:
            print('error load money')

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.id = object_as_dict['id']
        self.player_id = object_as_dict['player_id']
        self.achievement_id = object_as_dict['achievement_id']
        self.created = object_as_dict['created']
        return object_as_dict

    def __str__(self):
        return '{}(id={}, player_id={}, achivement_id={}, created={})'.format(
            self.__class__.__name__,
            self.id,
            self.player_id,
            self.achievement_id,
            self.created
        )
