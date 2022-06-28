class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library : {self.name} ")
        for book in self.bookslist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now.")
        else:
            print(f"this book is already been used by {self.lendDict[book]}")

    def addBook(self, book):
        self.bookslist.append(book)
        print("book has beenn added in the book list.")


    def rerturnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    harry = Library(['python', 'Rich daddy poor daddy', 'Do Epic Shit', 'Game of Thrones', 'Harry potter and the chamber of secrets', 'C++', 'Algorithms by CLRS '], "codewithharry")

    while(True):
        print(f"Welcome to {harry.name} library, Enter your choice to continue : ")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. add a Book")
        print("4. Return Books")
        user_choice = int(input())

        if user_choice==1:
            harry.displayBooks()

        elif user_choice==2:
            book = input("enter the book which you want to lend : ")
            user  =  input("Enter your name : ")
            harry.lendBook(user, book)
        elif user_choice==3:
            book = input("enter the book you want to add : ")
            harry. addBook(book)

        elif user_choice==4:
            book = input("enter the book you want to add : ")
            harry.rerturnBook(book)

        else:
            print("not a valid option")

        print("press Q to Quit and C to Continue : ")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2=="q":
                exit()

            elif user_choice2=="c":
                continue


