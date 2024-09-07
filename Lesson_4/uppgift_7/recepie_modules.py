def add_recepie(recepie_list:list):
    title = input("Enter the name of the dish:\n")
    ingredients_str = input("List the ingredients in a comma seperated text string:\n")
    ingredients = ingredients_str.split(",")
    instructions = input("Describe how to prepare the dish:\n")
    recepie = {"title": title, "ingredients":ingredients, "instructions":instructions}
    recepie_list.append(recepie)
    return recepie_list

def search_recepie(recepie_list:list):
    if recepie_list: #if lists are empty they are considered False
        query_matches = 0
        title = input("Enter the name of the dish:\n")
        for recepie in recepie_list:
            if recepie["title"] == title:
                query_matches += 1
                print(recepie)
        if query_matches == 0:
            print("No recepie with that title was found")
        else:
            print(f"{query_matches} recepies with that title found")
    else:
        print("Recepie list empty")

def list_recepies(recepie_list:list):
    if recepie_list: #if lists are empty they are considered False
        for recepie in recepie_list:
            print(recepie["title"])
    else:
        print("Recepie list empty")
