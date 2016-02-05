from player import Player

class Moderator(Player):
    def __init__(self, nick, login, password, additional_attribute=None):
        Player.__init__(self, nick, login, password)
        self.additional_attribute = additional_attribute

    def as_dict(self):
        d = Player.as_dict(self)
        d["additional_attribute"] = self.additional_attribute
        return d

    def load(self, file_object):
        object_as_dict = Player.load(self, file_object)
        self.additional_attribute = object_as_dict["additional_attribute"]
        return object_as_dict

    def __str__(self):
        return '{}(login="{}", additional_attribute="{}")'.format(self.__class__.__name__, self.login, self.additional_attribute)

    def send_in_the_ban(self):
        print('M M Monster kill')

    def clean_chat(self): ################???
        print('cleaning cleaning cleaning cleaning cleaning cleaning cleaning cleaning cleaning')

