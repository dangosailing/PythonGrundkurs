def add_recepie():
    title = input("Enter the name of the dish:\n")
    ingredients_str = input("List the ingredients in a comma seperated text string:\n")
    ingredients = ingredients_str.split("")
    instructions = input("Describe how to prepare the dish:\n")
    recepie = {"title": title, "ingredients":ingredients, "instructions":instructions}
    return recepie