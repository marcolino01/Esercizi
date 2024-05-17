class Book:

    def __init__(self, book_id: int, title : str, author: str, is_borrowed: bool):
        self.book_id : int = book_id
        self.title : str = title
        self.author : str = author
        self.is_borrowed : bool = is_borrowed

    def borrow():
        pass

    def return_book():
        pass


class Member():

    def __init__(self, member_id: int, name: str, borrowed_books: list[Book]):
        self.member_id : int = member_id
        self.name : str = name
        self.borrowed_books : list[Book] = borrowed_books

    def borrow_book(self,book):
        self.book = book


class Library():

    def __init__(self, books: dict[str, Book], title: str, author: str):
        self.books : dict[str, Book] = books
        self.title : str = title
        self.author : str = author
