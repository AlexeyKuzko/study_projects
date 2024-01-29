import pytest
from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        assert len(collector.get_books_genre()) == 2

    def test_init_attributes_equals_to_predefined_true(self):
        collector = BooksCollector()
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == [
            "Фантастика",
            "Ужасы",
            "Детективы",
            "Мультфильмы",
            "Комедии",
        ]
        assert collector.genre_age_rating == ["Ужасы", "Детективы"]

    @pytest.fixture(autouse=True)
    def collector(self):
        collector = BooksCollector()
        return collector

    # Happy Path Tests
    @pytest.mark.parametrize("name", ["Война и мир", "Анна Каренина", "Воскресение"])
    def test_add_new_book_book_name_added_true(self, name, collector):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize("name", ["", "A" * 41])
    def test_add_new_book_invalid_name_false(self, name, collector):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    @pytest.mark.parametrize(
        "name, genre",
        [("Дюна", "Фантастика"), ("Сияние", "Ужасы"), ("Убийство в Восточном экспрессе", "Детективы")],
    )
    def test_set_book_genre_name_equals_genre_true(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        "name, genre",
        [
            ("Алгебра и начала мат. анализа", "Учебники"),
            ("Мемуары гейши", "Мемуары"),
            ("Лирика А. Ахматовой", "Поэзия"),
        ],
    )
    def test_set_book_genre_invalid_genre_false(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert not collector.get_book_genre(name) == genre

    @pytest.mark.parametrize("genre", ["История", "Кулинария", "Поэмы"])
    def test_get_books_with_invalid_genre_false(self, genre, collector):
        collector.add_new_book("Пикник на обочине")
        collector.set_book_genre("Пикник на обочине", "Фантастика")
        books = collector.get_books_with_specific_genre(genre)
        assert "Пикник на обочине" not in books

    @pytest.mark.parametrize("genre", ["Фантастика", "Ужасы", "Детективы"])
    def test_get_books_with_specific_genre_name_returned_for_provided_genre_true(self, genre, collector):
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", genre)
        books = collector.get_books_with_specific_genre(genre)
        assert "Властелин колец" in books

    def test_get_books_for_children_name_returned_for_genre_without_age_rating_true(self, collector):
        collector.add_new_book("Алиса в стране чудес")
        collector.set_book_genre("Алиса в стране чудес", "Комедии")
        books = collector.get_books_for_children()
        assert "Алиса в стране чудес" in books

    @pytest.mark.parametrize("name", ["Гарри Поттер", "Три товарища", "Мастер и Маргарита"])
    def test_add_book_in_favorites_name_contained_in_favorites_true(self, name, collector):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        favorites = collector.get_list_of_favorites_books()
        assert name in favorites

    @pytest.mark.parametrize("name", ["50 оттенков серого", "Над пропастью во ржи", "Сумерки"])
    def test_delete_book_from_favorites_name_contained_in_favorites_false(self, name, collector):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        favorites = collector.get_list_of_favorites_books()
        assert name not in favorites
