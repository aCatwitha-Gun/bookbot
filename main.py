from stats import get_word_count
from stats import get_character_count
from stats import list_of_dictionaries_by_char
import sys

total_width = 50
report_header = " BOOKBOT ".center(total_width, '=')
report_word_count = " Word Count ".center(total_width, '-')
report_character_count = " Character Count ".center(total_width, '-')
report_footer = " END ".center(total_width, '=')

# function to get the file path of a book, then return the content of the book file as a string
def get_book_text(file): 
    with open(file) as f:   # open file as f
        book_text = f.read()    # set book_text to content of file as a string
    return book_text            # return the results

# function to run report after collecting book data
def run_report(file_path, word_count, sort_count):
    print(report_header)
    print(f"Analyzing book found at {file_path}...")
    print(report_word_count)
    print(f"Found {word_count} total words")
    print(report_character_count)
    # for each dictionary in list sort_count, print if char is an alphabetical character
    for i in sort_count:
        if i["char"].isalpha():
            char = i["char"]
            num = i["num"]

            print(f"{char}: {num}")

    print(report_footer)


# function to input file path of book
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_content = get_book_text(file_path)
    word_count = get_word_count(book_content)
    character_count = get_character_count(book_content)
    sort_count = list_of_dictionaries_by_char(character_count)
    # print(f"{word_count} words found in the document")
    # print(character_count)
    # print(sort_count)
    # print(run_report)
    run_report(file_path, word_count, sort_count)


main()

