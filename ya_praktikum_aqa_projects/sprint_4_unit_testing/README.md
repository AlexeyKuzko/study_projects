# qa_python

### Тесты, которые удалось реализовать
###### Каждый тест проверяет определенное поведение методов класса BooksCollector и содержит ожидаемые значения для успешного выполнения теста.

1. `test_add_new_book_add_two_books` - тестирует метод _**add_new_book**_, проверяет корректность добавления двух книг в коллекцию.
2. `test_init_attributes_equals_to_predefined_true` - тестирует инициализацию атрибутов экземпляра класса **_BooksCollector_**, проверяет их равенство заданным значениям.
3. `test_add_new_book_book_name_added_true` - тестирует метод **_add_new_book_**, проверяет, что добавленное имя книги присутствует в списке книг.
4. `test_add_new_book_invalid_name_false` - тестирует метод **_add_new_book_** с невалидными именами книг, проверяет, что невалидное имя не добавляется в список книг.
5. `test_set_book_genre_name_equals_genre_true` - тестирует метод **_set_book_genre_**, проверяет, что заданному имени книги соответствует указанный жанр.
6. `test_set_book_genre_invalid_genre_false` - тестирует метод **_set_book_genre_** с невалидными жанрами книг, проверяет, что жанр не соответствует заданному имени книги.
7. `test_get_books_with_invalid_genre_false` - тестирует метод **_get_books_with_specific_genre_**, проверяет, что книга с невалидным жанром не содержится в списке книг заданного жанра.
8. `test_get_books_with_specific_genre_name_returned_for_provided_genre_true` - тестирует метод **_get_books_with_specific_genre_**, проверяет, что книга с заданным жанром содержится в списке книг этого жанра.
9. `test_get_books_for_children_name_returned_for_genre_without_age_rating_true` - тестирует метод **_get_books_for_children_**, проверяет, что книга для детей содержится в списке книг без возрастного ограничения.
10. `test_add_book_in_favorites_name_contained_in_favorites_true` - тестирует метод **_add_book_in_favorites_**, проверяет, что добавленная книга содержится в списке избранных книг.
11. `test_delete_book_from_favorites_name_contained_in_favorites_false` - тестирует метод **_delete_book_from_favorites_**, проверяет, что удаленная книга больше не содержится в списке избранных книг.