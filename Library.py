# Mini Library App (Optimized + try/except + No __str__)

class Book:
    def __init__(self, name, price, pages):
        self.name = name
        self.price = price
        self.pages = pages
    
    def book_info(self):
        return f"Book: {self.name}, Price: {self.price}, Pages: {self.pages}"


class Library:
    def __init__(self):
        self.books = {}  # dictionary for fast lookup

    def add_book(self, book: Book):  # ✅ accept Book object
        if book.name in self.books:
            print("A book with this name already exists!")
            return
        self.books[book.name] = book
        print(f"Book '{book.name}' added successfully.")

    def remove_book(self, book: Book):  # ✅ accept Book object
        if book.name in self.books:
            del self.books[book.name]
            print(f"Book '{book.name}' removed successfully.")
        else:
            print("Book not found.")

    def search_book(self, book: Book):  # ✅ accept Book object
        if book.name in self.books:
            print("Book found:")
            print(self.books[book.name].book_info())
        else:
            print("Book not found.")

    def show_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        
        for book in self.books.values():
            print(book.book_info())


# ========================
#       MAIN PROGRAM
# ========================

library = Library()

while True:
    print("\nChoose an option:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Show All Books")
    print("5. Exit")

    choice = input("Enter choice: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue

    match choice:

        case 1:
            name = input("Enter book name: ")
            try:
                price = int(input("Enter price: "))
                pages = int(input("Enter page count: "))
            except ValueError:
                print("Price and pages must be numeric!")
                continue

            library.add_book(Book(name, price, pages))  # ✅ pass Book object

        case 2:
            name = input("Enter book name to remove: ")
            library.remove_book(Book(name, 0, 0))  # ✅ pass Book object (dummy price/pages)

        case 3:
            name = input("Enter book name to search: ")
            library.search_book(Book(name, 0, 0))  # ✅ pass Book object (dummy price/pages)

        case 4:
            library.show_all_books()

        case 5:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice. Please choose between 1 and 5.")
