from base_classes import Library

original_add_book = Library.add_book

def wrapped_add_book(self, title, author, page_amount):
    i = input("How many books do you want to enter?: ")
    while i>0:
        original_add_book(self, title, author, page_amount)
        i-=1

Library.add_book = wrapped_add_book