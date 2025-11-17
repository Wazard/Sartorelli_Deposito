import math

class Punto:
    def __init__(self, x ,y): # constructor, x and y coordinates
        self.x = x
        self.y = y
    
    def move(self,dx,dy,speed=1): # moves by given amount x and y and speed
        self.x += dx*speed
        self.y += dy*speed
    
    def distance_from_origin(self): # returns distance from (0,0)
        return math.sqrt(self.x**2+self.y**2)


class Libro:
    def __init__(self, title , author, page_amount): # constructor with title, author and page amount
        self.title = title
        self.author = author
        self.page_amount = page_amount

    def description(self): # description... describes the book
        return f"{self.title} book, written by {self.author} has {self.page_amount} amout of pages"

class Library:
    def __init__(self, name, address, books = []): # constructor
        self.name = name
        self.address = address
        self.books = books
    
    def add_book(self, title, author, page_amount): # adds a new book fromn scratch
        new_book = Libro(title, author, page_amount)
        if new_book in self.books:
            print(f"Book already in the Library")
            return
        self.books.append(new_book)
        print(f"{new_book.title} added to the {self.name} Library")
    
    def add_existing_book(self, book): # adds an already existing book
        if isinstance(book, Libro):
            self.books.append(book)
            print(f"{book.title} added to the {self.name} Library")

    def list_books(self): # prints all books
        print(book.description() for book in self.books)