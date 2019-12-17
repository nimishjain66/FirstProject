import json


books_file='books.json'
def create_book_table():
    with open(books_file,"w") as file:
        json.dump([],file)

def add_book(name,author):
    books=get_all_books()
    books.append({"name":name,"author":author,"read":False})
    _save_all_book(books)

def get_all_books():
    with open(books_file,'r') as file:
        return json.load(file)

def read_book(book_name):
    books=get_all_books()

    for book in books:
        if book['name']==book_name:
            book['read']=True
    _save_all_book(books)

def _save_all_book(books):
    with open(books_file,'w') as file:
        return json.dump(books,file)

def delete_book1(name1):
    books=get_all_books()
    books=[book for book in books if book['name']!=name1]
    _save_all_book(books)


