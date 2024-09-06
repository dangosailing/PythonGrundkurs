#test_list=["tslad", "saa aa", "ijofa", "ioew"]

def filter_str_char(list:str, character:str):
  new_user_list = []
  for string in list:
    if string.count(character) > 0:
      new_user_list.append(string)
  return new_user_list

#filter_str_list(test_list)

def filter_str_len(list:str, max_length:int):
  new_user_list = []
  for string in list:
    string = string.strip()
    print("specified length; ", max_length)
    print("string length; ", len(string))
    if max_length >= len(string): new_user_list.append(string)
  return new_user_list