import json

class PlayerAchievements:
    def __init__(self):
        pass

    def as_dict(self):
        d = {
            "type": self.__class__.__name__,

        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        # self.name = object_as_dict["name"]
        return object_as_dict

    def __str__(self):
        return '{}(blabla)'.format(self.__class__.__name__)
