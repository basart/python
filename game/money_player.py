import json
import datetime
import db

class MoneyPlayer(object):

    def __init__(self, id=None, player_id=None, name=None, amount=None):
        self.id = id
        self.player_id = player_id
        self.name = name
        self.amount = amount
        self.created = datetime.datetime.now()
        self.updated = self.created

    def as_dict(self):
        d = {
            'name_class': self.__class__.__name__,
            'id': self.id,
            'player_id': self.player_id,
            'name': self.name,
            'amount': self.amount,
            'created': self.created,
            'updated': self.updated
        }
        return d

    def save_to_db(self):
        cursor = db.connect.cursor()
        sql_data = self.as_dict()
        insert_query = 'insert into money (id, player_id, name, amount, created, updated)' \
            ' values (%(id)s, %(player_id)s, %(name)s, %(amount)s, %(created)s, %(updated)s)'
        update_query = 'update money ' \
            'set player_id=%(player_id)s, name=%(name)s, amount=%(amount)s, created=%(created)s, updated=%(updated)s ' \
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
        query_for_delete_money = 'delete from money where id=%(id)s'
        try:
            cursor.execute(query_for_delete_money, sql_data)
        except db.IntegrityError:
            print('error delete money')

    def load_from_db(self, player_id):
        cursor = db.connect.cursor()

        sql_data = {
            'player_id': player_id
        }
        query_for_load_money = 'select * from money where player_id=%(player_id)s'
        try:
            cursor.execute(query_for_load_money, sql_data)
            db_row = cursor.fetchone()
            self.id = db_row[0]
            self.player_id = db_row[1]
            self.name = db_row[2]
            self.amount = db_row[3]
            self.created = db_row[4]
            self.updated = db_row[5]
        except db.IntegrityError:
            print('error load money')

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.id = object_as_dict['id']
        self.player_id = object_as_dict['player_id']
        self.name = object_as_dict['name']
        self.amount = object_as_dict['amount']
        self.created = object_as_dict['created']
        self.updated = object_as_dict['updated']

    def __str__(self):
        return '{}(id={}, player_id={}, name={}, amount={}, created={}, updated={})'.format(
            self.__class__.__name__,
            self.id,
            self.player_id,
            self.name,
            self.amount,
            self.created,
            self.updated
        )

