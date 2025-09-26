def average_length(user_string):
    words = user_string.split()
    if words:  # Ensure the string is not empty
        avg = sum(len(word) for word in words) / len(words)
    else:
        avg = 0
    return avg


def word_count(user_string):
    words = user_string.split()
    if words:
        total_count = len(words)
    else:
        total_count = 0
    return total_count

def char_count(user_string):
    return len(user_string)

def longest_word(user_string):
    longest_word_len = 0
    words = user_string.split()
    long_word = None
    for word in words:
        if len(word) > longest_word_len:
            long_word = word
            longest_word_len = len(word)
        elif len(word) == longest_word_len:
            long_word = long_word + ", " + word
    return long_word