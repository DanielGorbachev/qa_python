import pytest

from main import BooksCollector
@pytest.fixture #создание новых книг
def add_three_new_books():
    add_three_new_books = BooksCollector()
    add_three_new_books.add_new_book("Homo Sapiens")
    add_three_new_books.add_new_book("Homo Sapiens Sapiens")
    add_three_new_books.add_new_book("Homo Ludens")
    return add_three_new_books
@pytest.fixture #создание 1 книги
def add_new_book():
    add_new_book = BooksCollector()
    add_new_book.add_new_book("Гарри Поттер")
    return add_new_book
@pytest.fixture #рандомизация рейтинга у трех книг
def three_different_rating_books(add_three_new_books):
    add_three_new_books.set_book_rating("Homo Sapiens Sapiens", 5)
    add_three_new_books.set_book_rating("Homo Ludens", 10)
    return add_three_new_books