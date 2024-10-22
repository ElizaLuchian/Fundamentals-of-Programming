import copy
import pickle
import random
import jsonpickle
import json
from src.domain import Student


class HistoryEmptyError(Exception):
    def __str__(self):
        return "History stack is empty."


class Repository:
    def __init__(self):
        self._students = []
        self._history = []

    def add_to_history(self):
        self._history.append(copy.deepcopy(self._students))

    def pop_history(self):
        if len(self._history) < 1:
            raise HistoryEmptyError()

        self._students = copy.deepcopy(self._history[-1])
        self._history.pop()

    def already_exists(self, _student: Student):
        """
        the function tests if the id of a student that's read from the console is unique
        :param _student: _student
        :return: a boolean value
        """

        for x in self._students:
            if _student.id_ == x.id_:
                return False
        return True

    def add_student(self, _student: Student):
        """

            Adds a new student  in the list and saves the file
            :param _student:  instance of the Student class
            :return: none
        """
        if self.already_exists(_student) is False:
            raise ValueError("Invalid option")
        else:
            self.add_to_history()
            self._students.append(_student)

    def add_student_from_generator(self, _student: Student):
        self._students.append(_student)

    def get_all_students(self):
        return self._students

    def remove_all_by_group(self, group):
        self.add_to_history()
        modified = 1

        while modified == 1:
            modified = 0
            for x in self._students:
                if x.group == group:
                    self._students.remove(x)
                    modified = 1

    pass


class MemoryRepository(Repository):
    def __init__(self):
        super().__init__()  ####apeleaza metoda din clasa parinte
        self.generate_students()

    def generate_students(self):
        str1 = ["Andreea", "Maria", "Ioana", "Alexandra", "Andrei", "Mihai", "George", "Ionut", "Vlad",
                "Cristian"]
        str2 = ["Popescu", "Luchian", "DarthVeder", "Grigorescu", "Lotescu", "Servus", "Seras", "Ion",
                "Vlateg", "Labo"]

        for i in range(1, 11):
            id = i
            first_name = random.choice(str1)
            last_name = random.choice(str2)
            group = random.randint(1, 10)

            self.add_student_from_generator(Student(id, first_name + " " + last_name, group))


class TextFileRepository(Repository):
    def __init__(self, file_name: str):
        super().__init__()

        self.__file_name = file_name

        self.load()

    def load(self):
        file = open(self.__file_name, "r")
        string_values = file.readlines()

        for value in string_values:
            parsed_values = value.split("|")
            self.add_student_from_generator(Student(int(parsed_values[0]), parsed_values[1], int(parsed_values[2])))

        file.close()

    def save(self):
        values = []

        for student in self._students:
            values.append(str(student.id_) + "|" + student.name + "|" + str(student.group) + "\n")

        file = open(self.__file_name, "w")
        file.writelines(values)
        file.close()

    def remove_all_by_group(self, value: int):
        super().remove_all_by_group(value)

        self.save()

    def add_student(self, value: Student):
        """
        "The function calls the method from the parent Class and then saves it to file
        :param value: value----instance from the Student Class
        :return: none
        """
        super().add_student(value)

        self.save()

    def pop_history(self):
        super().pop_history()

        self.save()


class BinaryRepository(Repository):
    def __init__(self, file_name: str):
        super().__init__()

        self.__file_name = file_name

        self.load()

    def load(self):
        file = open(self.__file_name, "rb")
        self._students = pickle.load(file)
        file.close()

    def save(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._students, file)
        file.close()

    def generate_students(self):
        str1 = ["Andreea", "Maria", "Ioana", "Alexandra", "Andrei", "Mihai", "George", "Ionut", "Vlad",
                "Cristian"]
        str2 = ["Popescu", "Luchian", "DarthVeder", "Grigorescu", "Lotescu", "Servus", "Seras", "Ion",
                "Vlateg", "Labo"]

        for i in range(0, 10):
            id = random.randint(1000, 9999)
            first_name = random.choice(str1)
            last_name = random.choice(str2)
            group = random.randint(1, 10)
            self.add_student_from_generator(Student(id, first_name + " " + last_name, group))

    def add_student(self, _student: Student):
        """
        The function calls the method from the parent Class and then saves it to file
        :param _student:
        :return: none
        """
        super().add_student(_student)
        self.save()

    def remove_all_by_group(self, group):
        super().remove_all_by_group(group)
        self.save()

    def pop_history(self):
        super().pop_history()
        self.save()


class JsonRepository(Repository):
    def __init__(self, file_name: str):
        super().__init__()

        self.__file_name = file_name

        self.load()

    def load(self):
        file = open(self.__file_name, "r")
        #first we load the json string from the file then we convert it to our object with pickle
        self._students = jsonpickle.decode(json.load(file))
        file.close()

    def save(self):
        file = open(self.__file_name, "w")
        #first we convert our object with pickle into a string then we save it onto the file
        json.dump(jsonpickle.encode(self._students), file)
        file.close()

    def add_student(self, _student: Student):
        """
        The function calls the method from the parent Class and then saves it to file
        :param _student:
        :return: none
        """
        super().add_student(_student)
        self.save()

    def remove_all_by_group(self, group):
        super().remove_all_by_group(group)
        self.save()

    def pop_history(self):
        super().pop_history()
        self.save()
