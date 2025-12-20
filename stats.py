#Count words in text
def count_words(text):
    words = text.split()
    return len(words)

#Count each characters in text
def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        #Only count alphabetic characters. Thanks to ChatGPT for this improvement
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count