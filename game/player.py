import json
import datetime
import db


class Player(object):
    def __init__(self, id=None, name=None, email=None, password=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.created = datetime.datetime.now()
        self.updated = self.created

    def as_dict(self):
        d = {
            'name_class': self.__class__.__name__,
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'created': self.created,
            'updated': self.updated
        }
        return d

    def save_to_db(self):
        cursor = db.connect.cursor()
        sql_data = self.as_dict()
        insert_query = 'insert into player (id, name, email, password, created, updated)' \
            ' values (%(id)s, %(name)s, %(email)s, %(password)s, %(created)s, %(updated)s)'
        update_query = 'update player ' \
            'set name=%(name)s, email=%(email)s, password=%(password)s, created=%(created)s, updated=%(updated)s ' \
            'where id=%(id)s'
        try:
            cursor.execute(insert_query, sql_data)
        except db.IntegrityError:
            sql_data['updated'] = datetime.datetime.now()
            cursor.execute(update_query, sql_data)
        db.connect.commit()

    def delete_from_db(self):
        cursor = db.connect.cursor()
        delete_query = 'delete from player where id=%(id)s'

        sql_data = {
            'id': self.id
        }
        try:
            cursor.execute(delete_query, sql_data)
        except:
            print('error delete player')

    def load_from_db(self, email):
        load_query = 'select id, name, email, password, created, updated ' \
                     'from player' \
                     ' where email=%(email)s'
        sql_data = {
            'email': email
        }
        cursor = db.connect.cursor()
        try:
            cursor.execute(load_query, sql_data)
            db_row = cursor.fetchone()
            self.id = db_row[0]
            self.name = db_row[1]
            self.email = db_row[2]
            self.password = db_row[3]
            self.created = db_row[4]
            self.updated = db_row[5]
        except TypeError:
            print('error load player')

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.id = object_as_dict['id']
        self.name = object_as_dict['name']
        self.email = object_as_dict['email']
        self.password = object_as_dict['password']
        self.created = object_as_dict['created']
        self.updated = object_as_dict['updated']

    def __str__(self):
        return '{}(id={}, name="{}", email="{}", password="{}", created={}, updated={})'.format(
            self.__class__.__name__,
            self.id,
            self.name,
            self.email,
            self.password,
            self.created,
            self.updated
        )


if __name__ == "__main__":
    player1 = Player(1, "noob", "noob@mail.ru", "3223")
    player1.save_to_db()
    # player1.delete_from_db()
    # player = Player()
    # player.load_from_db('noob@mail.ru')
    # player.delete_from_db()
    # player.save_to_db()
    # player.delete_from_db()
    # deserialized_player = Player()
    # deserialized_player.load(open("object_vasya@mail.ru.txt"))
    # print("deserialized player is {}".format(deserialized_player))
