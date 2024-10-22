from src.domain.rental import *
from src.repository.rentalrepo import *
from src.repository.movierepo import *
from src.repository.clientrepo import *

class EntityNotFoundError(Exception):
    def __init__(self, entity_name, entity_id):
        self.__entity_name = entity_name
        self.__entity_id = entity_id
    def __str__(self):
        return self.__entity_name + " with id " + str(self.__entity_id) + " not found"




class RentalService:
    def __init__(self, rental_repo: RentalRepo, movie_repo: MovieRepo, client_repo: ClientRepo):
        self.__repo = rental_repo
        self.__movie_repo = movie_repo
        self.__client_repo = client_repo

    def validate_movie(self, movie_id: int):
        found = False
        for el in self.__movie_repo.get_all_movies():
            if el.movie_id == movie_id:
                found = True

        if found is False:
            raise EntityNotFoundError("Movie", movie_id)

    def validate_client(self, client_id: int):
        found = False
        for el in self.__client_repo.get_all_clients():
            if el.client_id == client_id:
                found = True

        if found is False:
            raise EntityNotFoundError("Client", client_id)

        for rental in self.__repo.get_all_rentals_by_id(client_id):
            if rental.returned_date is not None and (rental.returned_date[0] + rental.returned_date[1] * 30 + rental.returned_date[2] * 365 >
                    rental.due_date[0] + rental.due_date[1] * 30 + rental.due_date[2] * 365):
                raise ValueError("Client is naspa")

    def add_rental(self, rental_id, movie_id: int, client_id: int, rented_date: [], due_date: []):
        self.validate_movie(movie_id)
        self.validate_client(client_id)

        self.__repo.add_rental(Rental(rental_id, movie_id, client_id, rented_date, due_date))

    def add_rental_class(self, rental: Rental):
        self.__repo.add_rental(rental)

    def return_rental(self, rental_id: int, returned_date: []):
        self.__repo.update_rental(rental_id, returned_date)

    def get_all_rentals(self):
        return self.__repo.get_all_rentals()

    def get_most_rented_movies(self):
        return self.__repo.most_rented_movies()

    def get_most_active_clients(self):
        return self.__repo.most_active_clients()

    def get_late_rentals(self):
        return self.__repo.late_rentals()

    def get_rental_by_id(self, id):
        return self.__repo.get_rental_by_id(id)

    def get_all_generated_rentals(self):
        list_of_rentals=Rental.generate_n_rentals(20)
        for rental in list_of_rentals:
            self.add_rental_class(rental)
        return list_of_rentals

















