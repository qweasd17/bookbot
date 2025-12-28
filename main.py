import sys
from stats import word_count, char_count, sort_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    content = get_book_text(file_path)
    report(file_path, word_count(content), sort_chars(char_count(content)))

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def report(file_path, num_words, chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for item in chars:
        if item["char"].isalpha():
            char = item["char"]
            num = item["num"]
            print(f"{char}: {num}")

main()