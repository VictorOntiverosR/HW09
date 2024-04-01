# Importing the BookLover class from your package
from Test.booklover import BookLover

def main():
    # Creating a BookLover object
    book_lover = BookLover(("Victor", "qfw3cr@virginia.edu", "Fiction")


    # Adding a book
    book_lover.add_book("Star Wars", 5)

    # Printing the number of books read
    print("Number of books read:", book_lover.num_books_read())

if __name__ == "__main__":
    main()