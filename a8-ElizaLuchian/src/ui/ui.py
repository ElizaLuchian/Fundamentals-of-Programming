from src.services.clientservice import ClientService
from src.services.movieservice import MovieService
from src.services.rentalservice import RentalService
from src.repository.clientrepo import *
from src.repository.movierepo import *
from src.repository.rentalrepo import *


class Ui:
    def __init__(self, client_service: ClientService, movie_service: MovieService, rental_service: RentalService):
        self.__client_service = client_service
        self.__movie_service = movie_service
        self.__rental_service = rental_service

    def print_menu(self):
        print("Insert an option:")
        print("1. Client menu")
        print("2. Movie menu")
        print("3. Rental menu")
        print("4. Search menu")
        print ("5. Statistics menu")
        # TO DO

        return input("> ")

    def print_client_menu(self):
        print("Insert sub-option:")
        print("1. Add a new entry")
        print("2. Remove a client")
        print("3. List all clients")
        print("4. Update client's name")

        return input(">")

    def print_movie_menu(self):
        print("Insert sub-option:")
        print("1. Add a new entry")
        print("2. Remove a movie")
        print("3. List all movies")
        print("4. Update movie's title")
        print("5. Update movie's description")
        print("6. Update movie's genre")

        return input(">")

    def print_rental_menu(self):
        print("Insert sub-option:")
        print("1. Add a new entry")
        print("2. Return a rental")
        print("3. List all rentals")

        return input(">")

    def print_search_menu(self):
        print("Insert sub-option:")
        print("1. Search upon movies")
        print("2. Search upon clients")

        return input(">")
    def print_statistics_menu(self):
        print("Insert sub-option:")
        print("1. Most rented movies")
        print("2. Most active clients")
        print("3. Late rentals")

        return input(">")

    def start(self):
        print("all generated clients")
        for x in self.__client_service.get_all_generated_clients():
            print(x)
        print("all generated movies")
        for x in self.__movie_service.get_all_generated_movies():
            print(x)
        print("all generated rentals")
        for x in self.__rental_service.get_all_generated_rentals():
            print(x)
        while True:
            try:
                print("-- Menu:")
                option = self.print_menu()

                if option == "1":
                    option = self.print_client_menu()
                    self.couple_client_option(option)
                elif option == "2":
                    option = self.print_movie_menu()
                    self.couple_movie_option(option)
                elif option == "3":
                    option = self.print_rental_menu()
                    self.couple_rental_option(option)
                elif option == "4":
                    option = self.print_search_menu()
                    self.couple_search_option(option)
                elif option =="5":
                    option= self.print_statistics_menu()
                    self.couple_statistics_option(option)
                elif option == "0":
                    exit()
            except Exception as ex:
                print(ex)

    def couple_client_option(self, option: str):
        if option == "1":
            client_id = input("Id: ")
            client_name = input("Name: ")
            self.__client_service.add_client(Client(int(client_id), client_name))
        elif option == "2":
            client_id = input("Id: ")
            self.__client_service.remove(int(client_id))
        elif option == "3":
            elements = self.__client_service.get_all_clients()
            for el in elements:
                print(el)
        elif option == "4":
            client_id = input("Id: ")
            client_name = input("Name: ")
            self.__client_service.update(int(client_id), client_name)
        else:
            print("Invalid option.")
            pass


    def couple_movie_option(self, option: str):
        if option == "1":
            movie_id = input("Id: ")
            title = input("Title")
            description = input("Description: ")
            genre = input("Genre: ")
            self.__movie_service.add_movie(Movie(int(movie_id), title, description, genre))
        elif option == "2":
            movie_id = input("Id: ")
            self.__movie_service.remove(int(movie_id))
        elif option == "3":
            elements = self.__movie_service.get_all_movies()
            for el in elements:
                print(el)
        elif option == "4":
            movie_id = input("Id: ")
            title = input("Title: ")
            self.__movie_service.update_title(int(movie_id), title)
        elif option == "5":
            movie_id = input("Id: ")
            description = input("Description: ")
            self.__movie_service.update_description(int(movie_id), description)
        elif option == "6":
            movie_id = input("Id: ")
            genre = input("Genre: ")
            self.__movie_service.update_genre(int(movie_id), genre)
        else:
            print("Invalid option.")
            pass

    def couple_rental_option(self, option: str):
        if option == "1":
            rental_id = input("Id: ")
            movie_id = input("Movie id: ")
            client_id = input("Client id: ")
            rented_date_raw = input("Rented date: ")
            due_date_raw = input("Due date: ")

            rented_date_args = rented_date_raw.split(' ')
            due_date_args = due_date_raw.split(' ')

            self.__rental_service.add_rental(
                int(rental_id), int(movie_id), int(client_id),
                [int(rented_date_args[0]), int(rented_date_args[1]), int(rented_date_args[2])],
                [int(due_date_args[0]), int(due_date_args[1]), int(due_date_args[2])])
        elif option == "2":
            rental_id = input("Id: ")
            returned_date_raw = input("Returned date: ")

            returned_date_args = returned_date_raw.split(' ')

            self.__rental_service.return_rental(
                int(rental_id),
                [int(returned_date_args[0]), int(returned_date_args[1]), int(returned_date_args[2])])
        elif option == "3":
            for el in self.__rental_service.get_all_rentals():
                print(el)

    def couple_search_option(self, option):
        if option == "1":
            search_string = input("Search string: ")
            for el in self.__movie_service.search(search_string):
                print(el)
        elif option == "2":
            search_string = input("Search string: ")
            for el in self.__client_service.search(search_string):
                print(el)
        else:
            print("Invalid option.")

    def couple_statistics_option(self, option):
        if option == "1":
            for el in self.__rental_service.get_most_rented_movies():
                print("Days: ", el[1], " for ", self.__movie_service.get_movie_by_id(el[0]))
        elif option == "2":
            for el in self.__rental_service.get_most_active_clients():
                print("Days: ", el[1], " for ", self.__client_service.get_client_by_id(el[0]))
        elif option == "3":
            for el in self.__rental_service.get_late_rentals():
                print("Days late: ", el[1], " for ", self.__rental_service.get_rental_by_id(el[0]))
        else:
            print("Invalid option.")


###############################################
movie_repo = MovieRepo()
client_repo = ClientRepo()
rental_repo = RentalRepo()

movie_service = MovieService(movie_repo)
client_service = ClientService(client_repo)
rental_service = RentalService(rental_repo, movie_repo, client_repo)

ui = Ui(client_service, movie_service, rental_service)

ui.start()
