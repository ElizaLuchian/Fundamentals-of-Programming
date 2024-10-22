from src.domain.movie import *
from src.repository.movierepo import *

class MovieService:
    def __init__(self, movie_repo: MovieRepo):
        self.__repo = movie_repo

    def add_movie(self, movie):
        self.__repo.add_movie(movie)

    def get_all_movies(self):
        return  self.__repo.get_all_movies()

    def remove(self, movie_id: int):
        self.__repo.remove(movie_id)

    def update_title(self, search_id: int, new_title):
        self.__repo.update_title(search_id,  new_title)

    def update_description(self, search_id: int, new_description):
        self.__repo.update_description(search_id, new_description)

    def update_genre(self, search_id: int, new_genre):
        self.__repo.update_genre(search_id, new_genre)

    def search(self, search_string: str):
        return self.__repo.search(search_string)

    def get_movie_by_id(self, id: int):
        return self.__repo.get_movie_by_id(id)
    def get_all_generated_movies(self):
        list_of_movies=Movie.generate_n_movies(20)
        for movie in list_of_movies:
            self.add_movie(movie)
        return list_of_movies

