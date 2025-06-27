import pytest
from src.bibliotheque.user import User
from src.bibliotheque.book import Book

class TestUser:
    def test_create_valid_user(self):
        user = User("Alice", "alice@email.com")
        assert user.name == "Alice"
        assert user.email == "alice@email.com"
        assert user.borrowed_books == []

    def test_create_user_invalid_email_raises_error(self):
        with pytest.raises(ValueError, match="@"):
            User("Alice", "aliceemail.com")

    def test_create_user_empty_name_raises_error(self):
        with pytest.raises(ValueError, match="nom"):
            User("", "alice@email.com")

    def test_can_borrow_limit(self):
        user = User("Bob", "bob@email.com")
        for i in range(3):
            user.add_borrowed_book(Book(f"Livre {i}", "Auteur", f"{i:013d}"))
        assert user.can_borrow() is False

    def test_add_and_remove_borrowed_book(self):
        user = User("Eve", "eve@email.com")
        book = Book("Titre", "Auteur", "1234567890123")
        user.add_borrowed_book(book)
        assert book in user.borrowed_books
        user.remove_borrowed_book(book)
        assert book not in user.borrowed_books
