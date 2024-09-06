def add_User(user_list:list):
  user_name = input("Enter your name")
  user_age = input("Enter your age")
  user = {"name":user_name, "age":user_age} 
  user_list.append(user)
  return user_list
