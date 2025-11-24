import sys
from stats import get_num_words, get_num_characters, get_num_characters_counter ,get_num_characters_new
from book import get_book_text

def main():
    print(sys.argv)
    print("============ BOOKBOT ============")
    path_to_file = sys.argv[1]
    print(f"Analyzing book found at {path_to_file}")
    text_book = get_book_text(path_to_file)
    num_words = get_num_words(text_book)
    char_dict = get_num_characters_new(text_book)

    #print(get_num_characters_counter(text_book))
    #print(get_num_characters(text_book))
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_list = char_dict.keys()
    for char in char_list:
        print(f"{char}: {char_dict[char]}")
    print("--------- END -------")



    
main()