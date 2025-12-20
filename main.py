from stats import count_words, count_characters
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    #Check for command line arguments
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    bookpath = sys.argv[1]

    # Get the text of the book
    book = get_book_text(bookpath)
    
    # Analyze the book
    num_words = count_words(book)
    char_counts = count_characters(book)
    
    # Print the results
    print ('============ BOOKBOT ============')
    print(f'Analyzing book found at {bookpath}...')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for char, count in char_counts.items():
        print(f"- '{char}: {count}'")
    print('============= END ===============')

main()