def count_words(content):
    my_list = content.split()
    num_words = len(my_list)
    return num_words

def count_chars(content):
    result = {}
    my_list = content.split()
    my_str = "".join(my_list)
    my_list = list(my_str)


    
    for i in range(0, len(my_list)):
        str = my_list[i].lower()

        if str not in result:
            result[str] = 0
        result[str] += 1
    return result

def sort_on(dict):
        return dict["num"]

def sorted_list(dict):
    my_list = []

    for key in dict:
         my_list.append({ "name": key, "num": dict[key] })

    my_list.sort(reverse=True, key=sort_on)
    return my_list
    

'''
def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
'''

        
'''
def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
'''
