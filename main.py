from stats import *
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
    top5_letters = top_n_common_letters(book, 5)
    top5_words = top_n_common_words(book, 5)
    least5_words = top_n_least_common_words(book, 5)
    top5_letters = top_n_common_letters(book, 5)

    
    # Print the results
    print ('============ BOOKBOT ============')
    print(f'Analyzing book found at {bookpath}...')
    print('-------Book Statistics:---------')
    print(f'Found {num_words} total words')
    print(f'Top 5 most common letters: {top5_letters}')
    print(f'Top 5 most common words: {top5_words}')
    print(f'Top 5 least common words: {least5_words}')
    print(f'Top 5 most common characters: {top5_letters}')
    print('-------Character counts:---------')
    for character in char_counts:
        if character.isalpha():
            print(f'Character counts: {character}: {char_counts[character]}')
    print('============= END ===============')

main()