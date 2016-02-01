import json
import datetime
import db

class CountersPlayer(object):
    def __init__(self):
        pass

    def as_dict(self):
        d = {
            "type": self.__class__.__name__,

        }
        return d

    def save_to_db(self):
        cursor = db.connect.cursor()
        dict_counters = self.as_dict()
        insert_query = 'insert into counters (id, name, email, password, created, updated)' \
                              ' values (%(id)s, %(name)s, %(email)s, %(password)s, %(created)s, %(updated)s)'
        update_query = 'update counters ' \
            'set name=%(name)s, email=%(email)s, password=%(password)s, created=%(created)s, updated=%(updated)s ' \
            'where id=%(id)s'
        try:
            cursor.execute(insert_query, dict_counters)
        except db.IntegrityError:

            dict_counters['updated'] = datetime.datetime.now()
            cursor.execute(update_query, dict_counters)
        db.connect.commit()

    def delete_from_db(self, id):
        cursor = db.connect.cursor()
        dict_counters = self.as_dict()
        delete_query = 'delete from counters where id=%(id)s'
        try:
            cursor.execute(delete_query, dict_counters)
        except db.IntegrityError:
            print('error delete counters')

    def load_from_db(self, id):
        cursor = db.connect.cursor()
        dict_counters = self.as_dict()
        load_query = 'select * from counters where player_id=%(player_id)s'
        try:
            cursor.execute(load_query, dict_counters)
            db_row = cursor.fetchone()
            self.id = db_row[0]
            self.player_id = db_row[1]
            self.name = db_row[2]
            self.amount = db_row[3]
            self.created = db_row[4]
            self.updated = db_row[5]
        except db.IntegrityError:
            print('error load counters')

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        # self.name = object_as_dict["name"]
        return object_as_dict

    def __str__(self):
        return '{}(blabla)'.format(self.__class__.__name__)
