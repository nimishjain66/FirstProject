from utils import Database_j
user_choice="""
Enter:
 - 'a' to add book
 - 'l' to get list of book
 - 'r' to mark as read
 - 'd' to delete the book
 - 'q' to quit
 
"""

def menue():
    Database_j.create_book_table()


    user_input=input(user_choice)
    while user_input!='q':
        if user_input=='a':
            call_add_book();

        elif user_input=='l':
            list_book()

        elif user_input=='r':
            mark_book()

        elif user_input=='d':
            delete_book()

        else:
            print("Unknown Command")

        user_input = input(user_choice)


def call_add_book():
    print("Enter the book details : ")
    name=input("Enter the name of the book : ")
    author=input("Enter the author : ")
    Database_j.add_book(name,author)



def list_book():
    books=Database_j.get_all_books()
    for book in books:
        read='YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read:{read}")


def mark_book():
    book_name=input("Enter the book name which u have read ")
    Database_j.read_book(book_name)

def delete_book():
    name1=input("Enter the name of the book : ")
    Database_j.delete_book1(name1)


menue()

