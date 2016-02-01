import json
import datetime
import db

class PlayerAchievements:
    def __init__(self):
        pass

    def as_dict(self):
        d = {
            "type": self.__class__.__name__,

        }
        return d

    def save_to_db(self):
        dict_achievements = self.as_dict()
        query_for_get_table = 'insert into achievements (id, name, email, password, created, updated)' \
                              ' values (%(id)s, %(name)s, %(email)s, %(password)s, %(created)s, %(updated)s)'
        try:
            self.dbcursor.execute(query_for_get_table, dict_achievements)
        except:
            query_for_get_table = 'update achievements ' \
            'set name=%(name)s, email=%(email)s, password=%(password)s, created=%(created)s, updated=%(updated)s ' \
            'where id=%(id)s'
            dict_achievements['updated'] = datetime.datetime.now()
            self.dbcursor.execute(query_for_get_table, dict_achievements)
        db.connect.commit()


    def delete_from_db(self, id):
        query_for_delete_achievements = 'delete from achievements where id={}'.format(id)
        try:
            self.dbcursor.execute(query_for_delete_achievements)
        except:
            pass

    def load_from_db(self, id):
        query_for_load_achievements = 'select * from achievements where id={}'.format(id)
        try:
            self.dbcursor.execute(query_for_load_achievements)
        except:
            pass

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        # self.name = object_as_dict["name"]
        return object_as_dict

    def __str__(self):
        return '{}(blabla)'.format(self.__class__.__name__)
