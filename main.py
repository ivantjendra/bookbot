# Import function count_words from file stats.py
from stats import count_words, count_chars, sorted_list
import sys

def get_book_text(filepath):
    # Open a file
    # with docs:
    # https://docs.python.org/3/reference/compound_stmts.html#with
    # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    with open(filepath) as f:
        # Read method to read the contents of a file into a string
        return f.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    count_result = count_words(file_contents)
    # print(f"{count_result} words found in the document")

    char_result = count_chars(file_contents)
    # print(char_result)

    sorted_result = sorted_list(char_result)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_result} total words")
    print("--------- Character Count -------")
    for el in sorted_result:
        name = el["name"]
        num = el["num"]

        if name.isalpha():
            print(f"{name}: {num}")
    print('============= END ===============')
main()

'''
from stats import get_num_words, get_chars_dict


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
'''

'''
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
'''