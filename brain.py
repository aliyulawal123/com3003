# print("Ready for the library")
# """ 
# 1. add new books to collection
# 2. allow memebers to borrow books
# 3. Allow members to return borrowed books
# 4. View list of books that are currenlty available. 
# """
# happy = {
#     1 : ["Harry Porter", "JK Rawlings"],
#     2: "Second entry"
# }

# #print(happy.keys(), happy.values())
# print(happy.get(1))

# class LibrarySystem(object):

#     name =  "Greenwood Community"

#     def  __init__(self, id, title, author):
#         self.id = id
#         self.title = title
#         self.author = author

#     def addBook(self, id, title, author):
#         self.shelf = {}
#         self.id = id
#         self.title = title
#         self.author = author
#         self.shelf.update({self.id:[self.title, self.author]})
#         print("Book Addedd Successfully")
#         print(self.shelf.keys(),self.shelf.get(self.id))
#         return self.shelf.get(self.id)


#     def borrow(self, id):
#         self.id = id
#         self.shelf.pop(self.id)
#         print(self.id, "Borrowed")
#         print(self.shelf)

#     def returnedBook(self, id):
#         #self.shelf = {}
#         self.id = id
#         self.shelf.update({self.id:[self.title, self.author]})
#         print("Book Return Successfully")
#         print(self.shelf.keys(),self.shelf.get(self.id))
#         return self.shelf.get(self.id)   

#     def showBooksAvailable(self):
#         print("Available Books")
#         print(self.shelf.items())
#         #print(self.shelf.keys(), self.shelf.values())
        

# s1 = LibrarySystem(1, "AI Trading", "Andrew Yang")
# s1.addBook(2, " Solar farms", " John Smith")
# #s1.borrow(2)
# s1.addBook(3, " Bear and Wolves", " Snow man")
# s1.addBook(4, " Cats and Dogs", "Tiger Stripes")
# s1.addBook(5, " AI and ML", "Brian Castle ")
# s1.showBooksAvailable()

class LibrarySystem:
    def __init__(self):
        self.name = "Greenwood Community"
        self.available_books = {}
        self.borrowed_books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.available_books:
            print("Book ID already exists.")
            return
        self.available_books[book_id] = {
            "title": title,
            "author": author
        }
        print(f"'{title}' added successfully.")

    def borrow_book(self, book_id):
        if book_id not in self.available_books:
            print("Book not available.")
            return
        self.borrowed_books[book_id] = self.available_books.pop(book_id)
        print(f"Book ID {book_id} borrowed successfully.")

    def return_book(self, book_id):
        if book_id not in self.borrowed_books:
            print("This book was not borrowed.")
            return
        self.available_books[book_id] = self.borrowed_books.pop(book_id)
        print(f"Book ID {book_id} returned successfully.")

    def show_available_books(self):
        print("\nAvailable Books")
        for book_id, details in self.available_books.items():
            print(
                f"ID: {book_id} | "
                f"{details['title']} | "
                f"{details['author']}"
            )
            
    def show_borrowed_books(self):
        print("\nBorrowed Books")
        for book_id, details in self.borrowed_books.items():
            print(
                f"ID: {book_id} | "
                f"{details['title']} | "
                f"{details['author']}"
            )
# Create library
library = LibrarySystem()
# Add books
library.add_book(1, "AI Trading", "Andrew Yang")
library.add_book(2, "Solar Farms", "John Smith")
library.add_book(3, "Bears and Wolves", "Snow Man")
library.add_book(4, "Cats and Dogs", "Tiger Stripes")
# View books
library.show_available_books()
# Borrow
library.borrow_book(2)
# View after borrowing
library.show_available_books()
library.show_borrowed_books()
# Return
library.return_book(2)
# View after return
library.show_available_books()