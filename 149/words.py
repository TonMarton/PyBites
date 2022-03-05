from string import ascii_lowercase

def sort_words_case_insensitively(words: list):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    return sorted(words, key=lambda word: 'zzzzzz' + word.lower() if word[0].isnumeric() else word.lower())