from moderator import Moderator


class Administrator(Moderator):
    def __init__(self, id=None, name=None, email=None, password=None, additional_attribute=None,
                 another_additional_attribute=None):
        Moderator.__init__(self, id, name, email, password, additional_attribute)
        self.another_additional_attribute = another_additional_attribute

    def as_dict(self):
        d = Moderator.as_dict(self)
        d["another_additional_attribute"] = self.another_additional_attribute
        return d

    def load(self, file_object):
        object_as_dict = Moderator.load(self, file_object)
        self.another_additional_attribute = object_as_dict["another_additional_attribute"]
        return object_as_dict

    def __str__(self):
        return '{}(login="{}", additional_attribute="{}", another_additional_attribute="{}")'.format(
            self.__class__.__name__, self.name, self.additional_attribute, self.another_additional_attribute
        )

    def to_set_the_status_of_moderator(self):
        print('Now you are moderator')
