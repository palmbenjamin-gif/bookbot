# Count words in text
def count_words(text):
    words = text.split()
    return len(words)

# Top N characters in text
def top_n_common_characters(text, n):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_chars[:n]

# Top N letters in text
def top_n_common_letters(text, n):
    text = text.lower()
    letter_count = {}
    for char in text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    sorted_letters = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_letters[:n]

# Top N most common words
def top_n_common_words(text, n):
    words = text.lower().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:n]

# Top N least common words
def top_n_least_common_words(text, n):
    words = text.lower().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_words = sorted(word_count.items(), key=lambda item: item[1])
    return sorted_words[:n]

# Count each characters in text
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