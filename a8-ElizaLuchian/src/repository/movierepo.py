from src.domain.movie import Movie

class NotUniqueMovieIdError(Exception):
    def __init__(self, movie_id):
        self.__movie_id = movie_id

    def __str__(self):
        return str(self.__movie_id) + " is not an unique movie id "

class NotFoundError(Exception):
    def __init__(self, entity_id):
        self.__entity_id = entity_id
    def __str__(self):
        return str(self.__entity_id) + " this id is not found"
class MovieRepo:

    def __init__(self):
        self._movielist = []

    def add_movie(self, movie:Movie):
        if self.already_exists_movie(movie) is False:
            raise NotUniqueMovieIdError(movie.movie_id)



        self._movielist.append(movie)
    def get_all_movies(self):
        return self._movielist

    def update_title(self, search_id, new_title):
        found=0
        for movie in self._movielist:
            if search_id == movie.movie_id:
                movie.title = new_title
                found=1
        if found==0:
            raise  NotFoundError(search_id)

    def update_description(self, search_id, new_description):
        found=0
        for movie in self._movielist:
            if search_id == movie.movie_id:
                movie.description = new_description
                found=1
        if found==0:
            raise NotFoundError(search_id)


    def update_genre(self, search_id, new_genre):
        found=0
        for movie in self._movielist:
            if search_id == movie.movie_id:
                movie.genre = new_genre
                found=1
        if found==0:
            raise NotFoundError(search_id)


    def remove(self, movie_id):
        found=0
        for movie in self._movielist:
            if movie_id == movie.movie_id:
                self._movielist.remove(movie)
                found=1
        if found==0:
            raise NotFoundError(movie_id)

    def search(self, search_string: str):
        result = []
        search_string = search_string.lower()
        for el in self._movielist:
            if search_string in el.title.lower() or search_string in el.description.lower() or search_string in el.genre.lower() or search_string in str(el.movie_id).lower():
                result.append(el)
        return result

    def get_movie_by_id(self, id: int):
        found=0
        for movie in self._movielist:

            if movie.movie_id == id:
                found = 1
                return movie
        if found==0:
            raise  NotFoundError(id)

    def already_exists_movie(self, movie: Movie):

        for x in self._movielist:
            if movie.movie_id == x.movie_id:
                return False
        return True