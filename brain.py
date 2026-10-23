print("Ready for the library")
""" 
1. add new books to collection
2. allow memebers to borrow books
3. Allow members to return borrowed books
4. View list of books that are currenlty available. 
"""
happy = {
    1 : ["Harry Porter", "JK Rawlings"],
    2: "Second entry"
}

#print(happy.keys(), happy.values())
print(happy.get(1))

class LibrarySystem(object):

    name =  "Greenwood Community"

    def  __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

    def addBook(self, id, title, author):
        self.shelf = {}
        self.id = id
        self.title = title
        self.author = author
        self.shelf.update({self.id:[self.title, self.author]})
        print("Book Addedd Successfully")
        print(self.shelf.keys(),self.shelf.get(self.id))
        return self.shelf.get(self.id)


    def borrow(self, id):
        self.id = id
        self.shelf.pop(self.id)
        print(self.id, "Borrowed")
        print(self.shelf)

    def returnedBook(self, id):
        pass

s1 = LibrarySystem(1, "AI Trading", "Andrew Yang")
s1.addBook(2, " Cats and horses", " John Smith")
s1.borrow(2)
s1.addBook(2, " Bear and Wolves", " Snow man")