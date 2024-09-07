def write_note():
    filename_base = input("Enter a filename: ")
    file_extension = ".txt"

    filename = filename_base + file_extension

    with open(filename, "a") as file:
        print("Write note to be stored: ")
        user_note = input(">>> ")
        file.write(f"{user_note}\n")
    return filename

def read_note(filename:str):
    with open(filename, "r") as file:
       user_file = file.read()
       print(user_file)

def clear_note(filename:str):
    open(filename, "w").close()
    print(f"{filename} cleared")