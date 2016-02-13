import json
import datetime
import db


class GameSession(object):
    def __init__(self, player_id=None):
        self.player_id = player_id
        self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()

    def as_dict(self):
        d = {
            "type": self.__class__.__name__,
            "player_id": self.player_id,
            "created": self.created,
            "updated": self.updated
        }
        return d

    def save_to_db(self):
        cursor = db.connect.cursor()
        sql_data = self.as_dict()
        insert_query = 'insert into session (player_id, created, updated)' \
            ' values (%(player_id)s, %(created)s, %(updated)s)'
        try:
            cursor.execute(insert_query, sql_data)
        except db.IntegrityError:
            insert_query = 'update session ' \
            'set player_id=%(player_id)s, updated=%(updated)s ' \
            'where player_id=%(player_id)s'
            sql_data['updated'] = datetime.datetime.now()
            cursor.execute(insert_query, sql_data)

    def delete_from_db(self):
        cursor = db.connect.cursor()
        sql_data = {
            'player_id': self.player_id
        }
        delete_query = 'delete from session where player_id=%(player_id)s'
        try:
            cursor.execute(delete_query, sql_data)
        except:
            print('error delete session')

    def load_from_db(self, player_id):
        cursor = db.connect.cursor()
        sql_data = {
            'player_id': player_id
        }
        load_query = 'select * from session where player_id=%(player_id)s'
        try:
            cursor.execute(load_query, sql_data)
            db_row = cursor.fetchone()
            self.id = db_row[0]
            self.player_id = db_row[1]
            self.created = db_row[2]
            self.updated = db_row[3]
        except TypeError:
            print('error load session. Session entry does not exist! ')

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.player_id = object_as_dict['player_id']
        self.created = object_as_dict['created']
        self.updated = object_as_dict['updated']

    def __str__(self):
        return '{}(player_id={}, created={}, updated_id={})'.format(
            self.__class__.__name__,
            self.player_id,
            self.created,
            self.updated
        )
