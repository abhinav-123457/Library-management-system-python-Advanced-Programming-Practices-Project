```bash
class Library:
    def __init__(self):
        self.books = ["Dune by Frank Herbert",
                      "A Brief History of Time",
                      "Geronimo Stilton: The Mummy with No Name",
                      "Harry Potter and the Chamber of Secrets",
                      "Robin Sharma: Who will Cry when you will Die"]
        self.issued_books = {}

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"'{book_name}' has been added to the library.\n")

    def display_books(self):
        if self.books:
            print("Available books in the library:")
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")
        else:
            print("No books are currently available in the library.")
        print()

    def issue_book(self, book_name, user):
        if book_name in self.books:
            self.books.remove(book_name)
            self.issued_books[book_name] = user
            print(f"'{book_name}' has been issued to {user}.\n")
        else:
            print(f"Sorry, '{book_name}' is either not available or has already been issued.\n")

    def return_book(self, book_name):
        if book_name in self.issued_books:
            user = self.issued_books.pop(book_name)
            self.books.append(book_name)
            print(f"'{book_name}' has been returned by {user}.\n")
        else:
            print(f"'{book_name}' was not issued by the library.\n")

    def issued_books_list(self):
        if self.issued_books:
            print("Issued books:")
            for book, user in self.issued_books.items():
                print(f"'{book}' issued to {user}")
        else:
            print("No books have been issued.")
        print()


def main():
    library = Library()

    while True:
        print("\n==== Library Management System ====")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Issued Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            book_name = input("Enter the name of the book to issue: ")
            user = input("Enter the name of the user: ")
            library.issue_book(book_name, user)

        elif choice == '4':
            book_name = input("Enter the name of the book to return: ")
            library.return_book(book_name)

        elif choice == '5':
            library.issued_books_list()

        elif choice == '6':
            print("Exiting Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
