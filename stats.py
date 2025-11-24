from collections import Counter

def get_num_words(text):
    return len(text.split(" "))


def get_num_characters(text):
    char_dict = dict()
    words = text.split(" ")
    for word in words:
        for character in word.lower(): 
            if character in char_dict:
                char_dict[character] += 1
            else:
                char_dict[character] = 1         
    return char_dict

def get_num_characters_counter(text):
    char_dict = Counter()
    words = text.split(" ")
    for word in words:
        char_dict.update(word.lower())
    return char_dict

def get_num_characters_new(text):
    char_dict = {}
    for c in text: 
        lower_c = c.lower()
        if lower_c in char_dict:
            char_dict[lower_c] += 1
        else:
            char_dict[lower_c] = 1         
    return char_dict