from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_cant_add_two_identical_books(self):
        books = BooksCollector()
        books.add_new_book('Гордость и предубеждение и зомби')
        books.add_new_book('Гордость и предубеждение и зомби')
        assert len(books.books_rating) == 1

    def test_set_book_rating_min_max(self, add_new_book):
        # min
        add_new_book.set_book_rating("Гарри Поттер", 1)
        assert add_new_book.get_book_rating("Гарри Поттер") == 1
        # max
        add_new_book.set_book_rating("Гарри Поттер", 10)
        assert add_new_book.get_book_rating("Гарри Поттер") == 10

    def test_set_book_rating_to_non_existing_book(self,add_new_book):
        add_new_book.set_book_rating("Хроники Нарнии", 9)
        assert add_new_book.get_book_rating("Хроники Нарнии") is not 9

    def test_set_book_rating_under_limit(self, add_new_book):
        add_new_book.set_book_rating("Гарри Поттер", 0)
        assert add_new_book.get_book_rating("Гарри Поттер") > 0

    def test_set_book_rating_above_limit(self, add_new_book):
        add_new_book.set_book_rating("Гарри Поттер", 11)
        assert add_new_book.get_book_rating("Гарри Поттер") < 10

    def test_get_books_with_specific_rating_two_books_with_rating_five(self, add_three_new_books):
        books = BooksCollector()
        add_three_new_books.set_book_rating("Homo Ludens", 10)
        add_three_new_books.set_book_rating("Homo Sapiens", 5)
        add_three_new_books.set_book_rating("Homo Sapiens Sapiens", 5)
        assert len(add_three_new_books.get_books_with_specific_rating(5)) == 2

    def test_get_books_rating_is_dict(self,three_different_rating_books):
        assert type(three_different_rating_books.get_books_rating()) == dict

    def test_add_book_in_favorites_and_delete(self, add_three_new_books, add_new_book):
        add_three_new_books.add_book_in_favorites("Homo Ludens")
        assert add_three_new_books.favorites == ["Homo Ludens"]
        add_three_new_books.delete_book_from_favorites("Homo Ludens")
        assert add_three_new_books.favorites == []

    def test_delete_book_from_favorites_not_favorite_book(self, add_three_new_books):
        add_three_new_books.add_book_in_favorites("Homo Ludens")
        add_three_new_books.delete_book_from_favorites("Homo Sapiens")
        assert "Homo Ludens" in add_three_new_books.favorites
        assert "Homo Sapiens" in add_three_new_books.books_rating

    def test_get_list_of_favorites_books_list_of_3_books(self, add_three_new_books):
        add_three_new_books.add_book_in_favorites("Homo Ludens")
        add_three_new_books.add_book_in_favorites("Homo Sapiens")
        add_three_new_books.add_book_in_favorites("Homo Sapiens Sapiens")
        assert len(add_three_new_books.get_list_of_favorites_books()) == 3