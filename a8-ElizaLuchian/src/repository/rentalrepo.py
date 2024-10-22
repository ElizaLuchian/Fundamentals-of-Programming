import copy
import time
from collections import defaultdict
from datetime import timedelta, datetime

import dateutil.utils

from src.domain.rental import Rental

class NotUniqueIdError(Exception):
    def __init__(self, rental_id):
        self.__rental_id = rental_id

    def __str__(self):
        return str(self.__rental_id) + " is not an unique id "

class RentalRepo:

    def __init__(self):
        self._rentallist = []
    def already_exists_rental_movie(self, rental: Rental):

        for x in self._rentallist:
            if x.rental_id == rental.rental_id:
                return False
        return True

    def add_rental(self, rental:Rental):
        if self.already_exists_rental_movie(rental) is False:
            raise NotUniqueIdError(rental.rental_id)

        else:

            self._rentallist.append(rental)

    def update_rental(self, rental_id: int, returned_date: []):
        for rental in self._rentallist:
            if rental.rental_id == rental_id:
                rental.returned_date = copy.deepcopy(returned_date)

    def get_all_rentals_by_id(self, client_id: int):
        elements = []
        for rental in self._rentallist:
            if rental.client_id == client_id:
                elements.append(rental)
        return elements

    def get_all_rentals(self):
        return self._rentallist

    def most_rented_movies(self):
        aux = defaultdict(lambda: [0, 0])
        for rental in self._rentallist:
            aux[rental.movie_id][0] = rental.movie_id
            due_date_conversion = rental.due_date[0] + rental.due_date[1] * 30 + rental.due_date[2] * 365
            rented_date_conversion = rental.rented_date[0] + rental.rented_date[1] * 30 + rental.rented_date[2] * 365

            aux[rental.movie_id][1] = aux[rental.movie_id][1] + due_date_conversion - rented_date_conversion

        sorted_array = sorted(aux.values(), reverse=True, key=lambda k: k[1])

        return sorted_array


    def most_active_clients(self):
        aux = defaultdict(lambda: [0, 0])
        for rental in self._rentallist:
            aux[rental.client_id][0] = rental.client_id

            due_date_conversion = rental.due_date[0] + rental.due_date[1] * 30 + rental.due_date[2] * 365
            rented_date_conversion = rental.rented_date[0] + rental.rented_date[1] * 30 + rental.rented_date[2] * 365

            aux[rental.client_id][1] = aux[rental.client_id][1] + due_date_conversion - rented_date_conversion

        sorted_array = sorted(aux.values(), reverse=True, key=lambda k: k[1])

        return sorted_array

    def late_rentals(self):
        aux = defaultdict(lambda: [0, 0])

        for rental in self._rentallist:
            if rental.returned_date is None:
                continue

            aux[rental.rental_id][0] = rental.rental_id


            due_date_conversion = rental.due_date[0] + rental.due_date[1] * 30 + rental.due_date[2] * 365
            returned_date_conversion = rental.returned_date[0] + rental.returned_date[1] * 30 + rental.returned_date[2] * 365

            aux[rental.rental_id][1] = returned_date_conversion - due_date_conversion

        sorted_array = sorted(aux.values(), reverse=True, key=lambda k: k[1])

        return sorted_array

    def get_rental_by_id(self, id):
        for rental in self._rentallist:
            if rental.rental_id == id:
                return rental

