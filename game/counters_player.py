import json
import datetime
import db


class CountersPlayer(object):
    def __init__(self, id=None, player_id=None, number_of_steps=0, number_of_strokes=0,
                 number_of_completed_missions=0):
        self.id = id
        self.player_id = player_id
        self.number_of_steps = number_of_steps
        self.number_of_strokes = number_of_strokes
        self.number_of_completed_missions = number_of_completed_missions
        self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()

    def as_dict(self):
        d = {
            'type': self.__class__.__name__,
            'id': self.id,
            'player_id': self.player_id,
            'number_of_steps': self.number_of_steps,
            'number_of_strokes': self.number_of_strokes,
            'number_of_completed_missions': self.number_of_completed_missions,
            'created': self.created,
            'updated': self.updated

        }
        return d

    def save_to_db(self):
        cursor = db.connect.cursor()
        sql_data = self.as_dict()
        insert_query = 'insert into counters (id, player_id, steps, strokes, completed_missions,created, updated)' \
            ' values (%(id)s, %(player_id)s, %(number_of_steps)s, %(number_of_strokes)s, ' \
            '%(number_of_completed_missions)s, %(created)s, %(updated)s)'
        update_query = 'update counters ' \
            'set player_id=%(player_id)s, steps=%(number_of_steps)s, strokes=%(number_of_strokes)s, ' \
            'completed_missions=%(number_of_completed_missions)s, updated=%(updated)s ' \
            'where id=%(id)s'
        try:
            cursor.execute(insert_query, sql_data)
        except db.IntegrityError:
            sql_data['updated'] = datetime.datetime.now()
            cursor.execute(update_query, sql_data)
        db.connect.commit()

    def delete_from_db(self):
        cursor = db.connect.cursor()
        sql_data = {
            'id': self.id
        }
        delete_query = 'delete from counters where id=%(id)s'
        try:
            cursor.execute(delete_query, sql_data)
        except db.IntegrityError:
            print('error delete counters')

    def load_from_db(self, player_id):
        cursor = db.connect.cursor()
        sql_data = {
            'player_id': player_id
        }
        load_query = 'select * from counters where player_id=%(player_id)s'
        try:
            cursor.execute(load_query, sql_data)
            db_row = cursor.fetchone()
            self.id = db_row[0]
            self.player_id = db_row[1]
            self.number_of_steps = db_row[2]
            self.number_of_strokes = db_row[3]
            self.created = db_row[4]
            self.updated = db_row[5]
        except TypeError:
            print('error load counters. Counters entry does not exist! ')

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.id = object_as_dict['id']
        self.player_id = object_as_dict['player_id']
        self.number_of_steps = object_as_dict['number_of_steps']
        self.number_of_strokes = object_as_dict['number_of_strokes']
        self.created = object_as_dict['created']
        self.updated = object_as_dict['updated']

    def __str__(self):
        return '{}(id={}, player_id={}, experience={}, number_of_steps={}, ' \
               'number_of_strokes={}, created={}, updated={})'\
            .format(
                self.__class__.__name__,
                self.id,
                self.player_id,
                self.number_of_steps,
                self.number_of_strokes,
                self.created,
                self.updated
            )

