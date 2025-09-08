def get_word_count(text):
    split_text = text.split(None)
    count = 0
    for words in split_text:
        count += 1
    return count

def get_char_dict(text):
    text = text.lower()
    char_dict= {}    

    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1    

    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    char_dict_list = []

    for d in dict:
        new_dict = {"name": d, "num": dict[d]}
        char_dict_list.append(new_dict)

    char_dict_list.sort(reverse=True, key=sort_on)

    return char_dict_list