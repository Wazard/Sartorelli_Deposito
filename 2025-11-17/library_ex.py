from base_classes import Library

original_add_book = Library.add_book

def wrapped_add_book(self):
    i:int = int(input("How many books do you want to enter?: "))
    while i>0:
        title = input("Book title: ")
        author = input("Book author: ")
        page_amount:int = int(input("Book page amount: "))
        original_add_book(self, title, author, page_amount)
        i-=1

library = Library("dawg", "dawg street")
library.add_book = wrapped_add_book(library)