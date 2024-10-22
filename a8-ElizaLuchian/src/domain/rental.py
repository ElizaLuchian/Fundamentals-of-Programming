import random


class Rental:
    def __init__(self, rental_id: int, movie_id: int, client_id: int, rented_date=None, due_date=None, returned_date=None):
        if rented_date is None:
            rented_date = [0, 0, 0]
        if due_date is None:
            due_date = [0, 0, 0]
        self.__rental_id=rental_id
        self.__movie_id=movie_id
        self.__client_id=client_id
        self.__rented_date=rented_date
        self.__due_date=due_date
        self.__returned_date=returned_date

    @property
    def rental_id(self):
        return self.__rental_id

    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def client_id(self):
        return self.__client_id

    @property
    def rented_date(self):
        return self.__rented_date

    @property
    def due_date(self):
        return self.__due_date

    @property
    def returned_date(self):
        return self.__returned_date

    @rented_date.setter
    def rented_date(self, val):
        self.__rented_date = val

    @due_date.setter
    def due_date(self, val):
        self.__due_date = val

    @returned_date.setter
    def returned_date(self, val):
        self.__returned_date = val

    def __str__(self):
        return ("rental id: " + str(self.__rental_id) + " | movie id: " + str(self.__movie_id) + " | client id: "+ str(self.__client_id)+ " | rented date: " + str(self. __rented_date)+ " | due date: " + str(self.__due_date)+" | returned date: "+ str(self.__returned_date))

    @staticmethod
    def generate_rentals(idd:int):




        id_ = idd
        movie_id_=random.randint(1,20)
        client_id=random.randint(1,20)

        rent_date_day = random.randint(1,30)
        rent_date_month= random.randint(1, 13)
        rent_date_year= random.randint(2010, 2015)

        due_date_day= random.randint(1, 30)
        due_date_month=random.randint(1, 13)
        due_date_year=rent_date_year+random.randint(1,3)





        return Rental(id_,movie_id_, client_id, [rent_date_day, rent_date_month, rent_date_year],[due_date_day, due_date_month, due_date_year] )

    @staticmethod
    def generate_n_rentals(n: int):
        arr = []
        for i in range(1,n+1):
            new = Rental.generate_rentals(i)
            arr.append(new)
        return arr