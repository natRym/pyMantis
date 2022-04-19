from sys import maxsize


class Project:
    def __init__(self, name=None, status=None, view_state=None, description=None, id=None):
        self.name = name
        self.status = status
        self.view_state = view_state
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s;%s" % (self.id, self.name, self.status, self.view_state, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
