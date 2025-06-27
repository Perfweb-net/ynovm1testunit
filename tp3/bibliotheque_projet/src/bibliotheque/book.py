class Book:
    """Représente un livre dans la bibliothèque"""

    def __init__(self, title, author, isbn):
        if not title:
            raise ValueError("Le titre ne doit pas être vide.")
        if not author:
            raise ValueError("L'auteur ne doit pas être vide.")
        if not isinstance(isbn, str) or len(isbn) != 13:
            raise ValueError("L'ISBN doit contenir exactement 13 caractères.")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

    def is_available(self):
        return not self.borrowed

    def borrow(self):
        if self.borrowed:
            return False
        self.borrowed = True
        return True

    def return_book(self):
        if not self.borrowed:
            return False
        self.borrowed = False
        return True
