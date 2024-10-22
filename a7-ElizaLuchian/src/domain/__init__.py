class Student:
    def __init__(self, id_: int, name: str, group: int):
        if id_<1:
            raise ValueError("Invalid input")
        self.__id = id_
        self.__name = name
        if group < 0:
            raise ValueError("Invalid input")
        self.__group = group

    @property
    def id_(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    def __str__(self):
        return ("student id: " + str(self.__id) + " name: " + str(self.__name) + " group: " + str(self.__group))

    __repr__ = __str__

    def __eq__(self, other):
        return self.id_ == other.id_ and self.name == other.name and self.group == other.group
