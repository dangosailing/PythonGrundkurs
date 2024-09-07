def add_book(book_list:list):
    book_title = input("Enter book title: ")
    book_author = input("Enter book author: ")
    book = {"title": book_title, "author": book_author, "available": True}
    book_list.append(book)
    return book_list

def lend_book(book_list:list):
    print("Available books: ")
    print("---------------------")
    for entry in book_list:
        if entry["available"]:
            print(f"Title: {entry["title"]}, {entry["author"]}")
    title_query = input("Enter the title of the book you wish to borrow: ")
    for entry in book_list:
        if entry["title"] == title_query and entry["available"]:
            will_lend = input(f"Do you wish to lend out {entry["title"]} by {entry["author"]}? (Y/N): ")
            if will_lend.lower() == "y":
                entry["available"] = False
    return book_list