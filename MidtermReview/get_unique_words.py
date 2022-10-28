PUNCTUATION = "!.?"

def get_unique_words(words):
    """ (str) -> list<str>
    Returns a list of the unique words in the string s.
    Ignores capitalization and punctuation.

	>>>get_unique_words("apple apple. apple banana apple.")
	>>>['apple', 'banana']

	>>>get_unique_words("apple apple!")
	>>>['apple']
    """
    uniques = []
    for word in words.split():
        word = word.lower().strip(PUNCTUATION)
        if word not in uniques:
            uniques.append(word)

    return uniques

