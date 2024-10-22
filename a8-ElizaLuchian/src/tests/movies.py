import unittest

from src.domain.movie import Movie
from src.repository.clientrepo import NotFoundError
from src.repository.movierepo import NotUniqueMovieIdError, MovieRepo


class TestMovieRepo(unittest.TestCase):

    def setUp(self):
        self.movie_repo = MovieRepo()

    def test_add_movie(self):
        # Test adding a new movie
        movie = Movie(movie_id=1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo.add_movie(movie)
        self.assertIn(movie, self.movie_repo.get_all_movies())

    def test_get_all_movies(self):
        # Test getting all movies from an empty repository
        self.assertEqual(self.movie_repo.get_all_movies(), [])

        # Test getting all movies after adding some movies
        movies = [
            Movie(movie_id=1, title="Movie 1", description="Description 1", genre="Action"),
            Movie(movie_id=2, title="Movie 2", description="Description 2", genre="Drama"),
            Movie(movie_id=3, title="Movie 3", description="Description 3", genre="Comedy")
        ]
        for movie in movies:
            self.movie_repo.add_movie(movie)
        self.assertEqual(self.movie_repo.get_all_movies(), movies)

    def test_update_title(self):
        # Test updating the title of an existing movie
        movie = Movie(movie_id=1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo.add_movie(movie)
        new_title = "Updated Title"
        self.movie_repo.update_title(movie.movie_id, new_title)
        self.assertEqual(movie.title, new_title)

    def test_update_description(self):
        # Test updating the description of an existing movie
        movie = Movie(movie_id=1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo.add_movie(movie)
        new_description = "Updated Description"
        self.movie_repo.update_description(movie.movie_id, new_description)
        self.assertEqual(movie.description, new_description)

    def test_update_genre(self):
        # Test updating the genre of an existing movie
        movie = Movie(movie_id=1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo.add_movie(movie)
        new_genre = "Updated Genre"
        self.movie_repo.update_genre(movie.movie_id, new_genre)
        self.assertEqual(movie.genre, new_genre)

    def test_remove(self):
        # Test removing an existing movie
        movie = Movie(movie_id=1, title="The Great Movie", description="A fantastic movie", genre="Action")
        self.movie_repo.add_movie(movie)
        self.movie_repo.remove(movie.movie_id)
        self.assertNotIn(movie, self.movie_repo.get_all_movies())


if __name__ == '__main__':
    unittest.main()
