class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'

class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == "__main__":
    library = Library()
    book1 = Book(id_=library.get_next_book_id(), name='Война и мир', pages=1225)
    library.books.append(book1)

    book2 = Book(id_=library.get_next_book_id(), name='1984', pages=328)
    library.books.append(book2)

    book3 = Book(id_=library.get_next_book_id(), name='Преступление и наказание', pages=430)
    library.books.append(book3)

    book4 = Book(id_=library.get_next_book_id(), name='Мастер и Маргарита', pages=400)
    library.books.append(book4)

    for book in library.books:
        print(book)

    print(repr(book1))

    print(library.get_next_book_id())
    print(library.get_index_by_book_id(1))

