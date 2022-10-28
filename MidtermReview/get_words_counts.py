PUNCTUATION = ",!.?"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def get_word_count(s,w):
    """ (str, str) -> int
    Returns the number of times the word w appears in s.
    Ignores the capitalization and punctuation.
    """
    
    counter = 0
    for word in s.split():
        if word.lower().strip(PUNCTUATION) == w.lower().strip(PUNCTUATION):
            counter += 1
    return counter

def get_words_counts(s):
    """ (str) -> list<int>
    Returns a list of the counts of each word in s.
    Ignores capitalization and punctuation
    """
    
    if type(s) != str:
        raise ValueError("s must be a string.")
    
    for c in s:
        if c not in ALPHABET and c not in PUNCTUATION and c != " ":
            raise ValueError("Invalid character:", c)
    
    counts = []
    for word in s.split():
        word = word.lower().strip(PUNCTUATION)
        counts.append(get_word_count(s, word))
    return counts

