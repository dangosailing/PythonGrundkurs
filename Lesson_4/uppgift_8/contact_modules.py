def add_contact(contact_list:list):
    name = input("Enter a contact name: ").strip()
    tel_number = input("Enter their phone number: ").strip()
    new_contact = {"name": name, "telephone_number": tel_number}
    contact_list.append(new_contact)
    return contact_list

def list_contacts(contact_list:list):
    for entry in contact_list:
        print(f"name: {entry["name"]}, phone number:{entry["telephone_number"]}")

def search_contacts(contact_list:list):
    name_query = input("Search for a name in the contact book: ").strip()
    for entry in contact_list:
        if entry["name"] == name_query:
            print(f"name: {entry["name"]}, phone number:{entry["telephone_number"]}")
        else:
            print("No contact with that name was found")

contact_test=[]
contact_test = add_contact(contact_test)
list_contacts(contact_test)
search_contacts(contact_test)