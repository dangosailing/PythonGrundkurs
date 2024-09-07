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

def return_book(book_list:list):
    print("Boks to be returned: ")
    print("---------------------")
    for entry in book_list:
        if not entry["available"]:
            print(f"Title: {entry["title"]}, {entry["author"]}")
    title_query = input("Enter the title of the book you wish to return: ")
    for entry in book_list:
        if entry["title"] == title_query and not entry["available"]:
            will_return = input(f"Do you wish to return {entry["title"]} by {entry["author"]}? (Y/N): ")
            if will_return.lower() == "y":
                entry["available"] = True
    return book_list