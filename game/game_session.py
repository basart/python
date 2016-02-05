import json
import datetime
import db


class GameSession(object):
    def __init__(self, id=None, player_id=None):
        self.id = id
        self.player_id = player_id
        self.created = created
        self.updated = updated

    def as_dict(self):
        d = {
            "type": self.__class__.__name__,
            "id": self.id,
            "player_id": self.player_id,
            "created": self.created,
            "updated": self.updated
        }
        return d

    def save_to_db(self):
        cursor = db.connect.cursor()
        sql_data = self.as_dict()
        insert_query = 'insert into session (id, player_id created, updated)' \
                              ' values (%(id)s, %(player_id)s, %(created)s, %(updated)s)'
        try:
            cursor.execute(insert_query, sql_data)
        except db.IntegrityError:
            insert_query = 'update session ' \
            'set player_id=%(player_id)s, created=%(created)s, updated=%(updated)s ' \
            'where id=%(id)s'
            sql_data['updated'] = datetime.datetime.now()
            cursor.execute(insert_query, sql_data)
        db.connect.commit()

    def delete_from_db(self):
        cursor = db.connect.cursor()
        sql_data = {
            'id': self.id
        }
        delete_query = 'delete from session where id=%(id)s'
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
        except db.IntegrityError:
            print('error load session')

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.id = object_as_dict['id']
        self.player_id = object_as_dict['player_id']
        self.created = object_as_dict['created']
        self.updated = object_as_dict['updated']
        return object_as_dict

    def __str__(self):
        return '{}(id={}, player_id={}, created={}, updated_id={})'.format(
            self.__class__.__name__,
            self.id,
            self.player_id,
            self.created,
            self.updated
        )
