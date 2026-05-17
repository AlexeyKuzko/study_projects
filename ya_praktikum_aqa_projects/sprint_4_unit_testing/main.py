"""Main module for Yandex Praktikum Automation QA projects: Sprint 4 Unit Testing."""


class BooksCollector:
    """Collect books, genres, and favorites for unit-testing practice."""

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"]
        self.genre_age_rating = ["Ужасы", "Детективы"]

    # добавляем новую книгу
    def add_new_book(self, name):
        """Add the new book."""
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ""

    # устанавливаем книге жанр
    def set_book_genre(self, name, genre):
        """Set the book genre."""
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    # получаем жанр книги по её имени
    def get_book_genre(self, name):
        """Return the book genre."""
        return self.books_genre.get(name)

    # выводим список книг с определённым жанром
    def get_books_with_specific_genre(self, genre):
        """Return the books with specific genre."""
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    # получаем словарь books_genre
    def get_books_genre(self):
        """Return the books genre."""
        return self.books_genre

    # возвращаем книги, подходящие детям
    def get_books_for_children(self):
        """Return the books for children."""
        books_for_children = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books_for_children.append(name)
        return books_for_children

    # добавляем книгу в Избранное
    def add_book_in_favorites(self, name):
        """Add the book in favorites."""
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    # удаляем книгу из Избранного
    def delete_book_from_favorites(self, name):
        """Delete the book from favorites."""
        if name in self.favorites:
            self.favorites.remove(name)

    # получаем список Избранных книг
    def get_list_of_favorites_books(self):
        """Return the list of favorite books."""
        return self.favorites
