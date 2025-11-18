import __init__
from Utilities import functions


class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def description(self):
        return f"{self.title} book, written by {self.author}, isbn={self.isbn}"

    def __repr__(self):
            return self.description()


class Library:
    def __init__(self):
        self.catalogue = []  # catalogue will store Book objects

    def add_book(self, book):
        self.catalogue.append(book)

    def remove_book(self, book=None, isbn=None):
        if not functions.at_least_one_present(book=book, isbn=isbn):
            print("Removal failed: no book or isbn specified")
            return None

        # Remove by Book object
        if book is not None:
            for i, b in enumerate(self.catalogue):
                if b.isbn == book.isbn:
                    removed_book = self.catalogue.pop(i)
                    print(f"Removed: {removed_book}")
                    return removed_book
            print("Book not found in catalogue")
            return None

        # Remove by ISBN
        for i, b in enumerate(self.catalogue):
            if b.isbn == isbn:
                removed_book = self.catalogue.pop(i)
                print(f"Removed: {removed_book}")
                return removed_book
        print("Book not found in catalogue")
        return None

    def search_by_title(self, title: str):
        return [b for b in self.catalogue if b.title.lower() == title.lower()]

    def get_catalogue(self):
        return "\n".join(str(book) for book in self.catalogue)


# Create some books
book1 = Book("The Pragmatic Programmer", "Andrew Hunt & David Thomas", "978-0201616224")
book2 = Book("Clean Code", "Robert C. Martin", "978-0132350884")
book3 = Book("Design Patterns", "Erich Gamma et al.", "978-0201633610")
book4 = Book("Refactoring", "Martin Fowler", "978-0201485677")
book5 = Book("Code Complete", "Steve McConnell", "978-0735619678")

# Create library and add books
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

print("Initial catalogue:")
print(library.catalogue)

print("\nSearch by title 'Refactoring':")
print(library.search_by_title("Refactoring"))

# Remove by Book object
library.remove_book(book=book3)   # remove "Design Patterns"
library.remove_book()             # remotion failed

print(f"\nCatalogue after removing {book3} by Book object:")
print(library.get_catalogue())

isbn = "978-0132350884"
# Remove by ISBN (still works)
library.remove_book(isbn=isbn)  # remove "Clean Code"

print(f"\nFinal catalogue after removing {isbn} by ISBN:")
print(library.get_catalogue())