import sys
from stats import print_num_chars, get_num_words


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(book_path)
    print("--------- Character Count -------")
    print_num_chars(book_path)
    print("============= END ===============")


main()
