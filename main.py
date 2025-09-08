import sys
from stats import (
    get_word_count,
    get_char_dict,
    sort_dict,
)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_dict:
        if dict["name"].isalpha():
            print(f"{dict["name"]}: {dict["num"]}")    
    print("============= END ===============")

def main():    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    chars_dict = get_char_dict(book_text)
    sorted_dict = sort_dict(chars_dict)

    print_report(book_path, num_words, sorted_dict)
    
main()