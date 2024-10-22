from src.services import Services


class Ui:
    def __init__(self, services: Services):
        self.__services = services

    def print_menu(self):
        print("1. Add a student. Student data is read from the console.")
        print("2.Display the list of students.")
        print("3. Filter the list so that students in a given group (read from the console) are deleted from the list.")
        print("4. Undo the last operation that modified program data. This step can be repeated. "
              "The user can undo only those operations made during the current run of the program.")

    def get_input(self):
        return input(">")


    def get_option(self):
        option = int(self.get_input())

        if option == 1:
            id = input("Id: ")
            fname = input("First name: ")
            lname = input("Last name: ")
            group = input("Group: ")
            self.__services.add_student(id, fname + " " + lname, group)

        elif option == 2:
            for x in self.__services.get_all_students():
                print(x)

        elif option == 3:
            group = input("Group: ")
            self.__services.remove_students_from_group(group)

        elif option == 4:
            self.__services.undo()

        elif option == 0:
            exit()

        else:
            print(" Invalid choice")

    def start(self):

        while True:
            try:
                self.print_menu()
                self.get_option()
            except Exception as ex:
                print(ex)



    pass
