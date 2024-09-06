def add_user(user_list:list):
  user_name = input("Enter your name")
  user_age = input("Enter your age")
  user = {"name":user_name, "age":user_age} 
  user_list.append(user)
  return user_list

def search_user(user_list:list, user_name):
  found_user_list = []
  if len(user_list) > 0:
    for user in user_list:
      if user["name"] == user_name:
        print(f"name: {user["name"]} age: {user["age"]}")
        found_user_list.append(user)
    return found_user_list
  