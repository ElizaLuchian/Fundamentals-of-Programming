import unittest

from src.domain import Student
from src.repository import Repository, TextFileRepository, BinaryRepository


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.__repo = Repository()
        self.__repo2 = TextFileRepository("repotexttest.txt")
        self.__repo3 = BinaryRepository("repobinarytest.bin")
    def test_add(self):
        #Arrange
        student = Student(len(self.__repo.get_all_students()) + 1, "test", 1)
        expected_result = self.__repo.get_all_students() + [student]

        #Act
        self.__repo.add_student(student)

        #Assert
        self.assertEqual(self.__repo.get_all_students(), expected_result)
    def test_add2(self):
        #Arrange
        student = Student(len(self.__repo2.get_all_students()) + 1, "Maria Ioana", 2)
        expected_result = self.__repo2.get_all_students() + [student]

        #Act
        self.__repo2.add_student(student)

        #Assert
        self.assertEqual(self.__repo2.get_all_students(), expected_result)
    def test_add3(self):
        #Arrange
        student = Student(len(self.__repo3.get_all_students()) + 1, "Luchian Eliza", 3)
        expected_result = self.__repo3.get_all_students() + [student]

        #Act
        self.__repo3.add_student(student)

        #Assert
        self.assertEqual(self.__repo3.get_all_students(), expected_result)


if __name__ == '__main__':
    unittest.main()
