import json

class MoneyPlayer(object):

    def __init__(self, total_number_of_gold=100, total_number_of_silver=1000):
        self.total_number_of_gold = total_number_of_gold
        self.total_number_of_silver = total_number_of_silver
        self._coefficient_silver_to_gold = 0.1

    def as_dict(self):
        d = {
            "type": self.__class__.__name__,
            "total_number_of_gold": self.total_number_of_gold,
            "total_number_of_silver": self.total_number_of_silver
        }
        return d

    def save(self, file_object):
        json.dump(self.as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        # self.name = object_as_dict["name"]
        return object_as_dict

    def __str__(self):
        return '{}(total_number_of_gold="{}", total_number_of_silver="{}")'.format(
            self.__class__.__name__, self.total_number_of_gold, self.total_number_of_silver
        )

    def silver_to_gold(self, number_of_silver):
        self.total_number_of_gold += self._coefficient_silver_to_gold * number_of_silver
        self.total_number_of_silver -= number_of_silver