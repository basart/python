import json
import datetime
import db


class MoneyPlayer(object):
    def __init__(self, player_id=None):
        self.player_id = player_id
        self._money = {'gold': 100, 'silver': 100}
        self.created = datetime.datetime.now()
        self.updated = self.created

    def as_dict(self):
        d = {
            'name_class': self.__class__.__name__,
            'player_id': self.player_id,
            'money': self._money,
            'created': self.created,
            'updated': self.updated
        }
        return d

    def save_to_db(self):
        cursor = db.connect.cursor()

        insert_query = 'insert into money (player_id, name, amount, created, updated)' \
            ' values (%(player_id)s, %(name)s, %(amount)s, %(created)s, %(updated)s)'
        update_query = 'update money ' \
            'set player_id=%(player_id)s, name=%(name)s, amount=%(amount)s, updated=%(updated)s ' \
            'where id=%(id)s'
        for name in self._money:
            sql_data = {
                'player_id': self.player_id,
                'name': name,
                'amount': self._money[name],
                'created': self.created,
                'updated': self.updated
            }
            try:
                cursor.execute(insert_query, sql_data)
            except db.IntegrityError:
                sql_data['updated'] = datetime.datetime.now()
                cursor.execute(update_query, sql_data)
            db.connect.commit()

    def delete_from_db(self):
        cursor = db.connect.cursor()
        sql_data = {
            'id': self.player_id
        }
        query_for_delete_money = 'delete from money where player_id=%(player_id)s'
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
            db_rows = cursor.fetchall()
            money_player = {}
            for row in db_rows:
                money_player[row[2]] = row[3]
            return money_player
        except db.IntegrityError:
            print('error load money')
        except TypeError:
            print('error load money. Money entry does not exist! ')

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.player_id = object_as_dict['player_id']
        self._money = object_as_dict['money']
        self.created = object_as_dict['created']
        self.updated = object_as_dict['updated']

    def __str__(self):
        return '{}(player_id={}, money={}, created={}, updated={})'.format(
            self.__class__.__name__,
            self.player_id,
            self._money,
            self.created,
            self.updated
        )

if __name__ == '__main__':
    money = MoneyPlayer(1)
    money = money.load_from_db(1)
    print(money)
