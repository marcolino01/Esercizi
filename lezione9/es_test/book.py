class Book:

    def __init__(self, book_id: str, title : str, author: str):
        self.book_id : str = book_id
        self.title : str = title
        self.author : str = author
        self.is_borrowed : bool = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
    

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False


class Member():

    def __init__(self, member_id: int, name: str):
        self.member_id : int = member_id
        self.name : str = name
        self.borrowed_books : list[Book] = []

    def borrow_book(self, book: Book):
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.borrow()

    def return_book(self, book: Book):
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.return_book()


class Library():

    def __init__(self, books : dict[str, Book]={}, members : dict[str, Member]={}):
        self.books : dict[str, Book] = books
        self.members : dict[str, Member] = members

    def add_book(self, book_id: str, title: str, author: str):
        book = Book(book_id, title, author)
        if book_id not in self.books:
            self.books[book_id] = book

    def register_member(self,member_id: str, name : str):
        if member_id not in self.members:
            new_member: Member = Member(member_id, name)
            self.members[member_id] = new_member

    def borrow_book(self, member_id: str, book_id: str):
        if book_id in self.books.keys():
            this_book: Book = self.books[book_id]
            if member_id in self.members.keys():
                this_member: Member = self.members[member_id]
                this_member.borrow_book(this_book)
    

    def return_book(self, member_id: str, book_id: str):
        if book_id in self.books.keys():
            this_book: Book = self.books[book_id]
            if member_id in self.members.keys():
                this_member: Member = self.members[member_id]
                this_member.return_book(this_book)
        
    def get_borrowed_books(self, member_id: str):
        this_member: Member = self.members.get(member_id, None)
        if this_member:
            titles: list[str] = [borrowed_book.title for borrowed_book in this_member.borrowed_books]   #comprehension del ciclo for sotto
            """for borrowed_book in this_member.borrowed_books:
                titles.append(borrowed_book.title)"""
            return titles