def add_book(book_list:list):
    book_title = input("Enter book title: ")
    book_author = input("Enter book author: ")
    book = {"title": book_title, "author": book_author}
    book_list.append(book)
    return book_list