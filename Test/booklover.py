import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame(columns=['book_name', 'book_rating'])

    def add_book(self, book_name, rating):
        if not self.book_list['book_name'].str.contains(book_name).any():
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            print(f"{book_name} has been added to {self.name}'s book list with a rating of {rating}.")
        else:
            print(f"{self.name} has already read {book_name}.")

    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]