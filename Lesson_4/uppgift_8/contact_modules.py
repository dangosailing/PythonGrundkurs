def add_contact(contact_list:list):
    name = input("Enter a contact name: ")
    tel_number = input("Enter their phone number: ")
    new_contact = {"name": name, "telephone_number": tel_number}
    contact_list.append(new_contact)
    return contact_list