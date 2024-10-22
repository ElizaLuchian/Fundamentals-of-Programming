from src.domain import *
from src.repository import *


class Services:
    def __init__(self, repo: Repository):
        self.__repo = repo

    def add_student(self, id, name, group):
        """
        the function is a method which initially validates and sends error and if there are no errors, it calls the method from the repo

        :param id: student id
        :param name: student name
        :param group: student group
        :return: none
        """
        if id.isnumeric() is False or int(id) < 1:
            raise ValueError("Invalid id inserted")
        if name.isnumeric():
            raise ValueError("Invalid name is inserted")
        if group.isnumeric() is False or int(group) < 1:
            raise ValueError("Invalid group inserted")
        self.__repo.add_student(Student(int(id), name, int(group)))

    def get_all_students(self):
        return self.__repo.get_all_students()

    def remove_students_from_group(self, group):
        if group.isnumeric() is False or int(group) < 1:
            raise ValueError("Invalid group inserted")

        self.__repo.remove_all_by_group(int(group))

    def undo(self):
        self.__repo.pop_history()

    pass
