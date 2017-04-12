"""
Generate markov text from text files.
"""

from random import choice


def open_and_read_file(file_path):
    """
    
    Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and 
    Turns the file's contents as one string of text.
    
    """

    # read the file, return text as a string titled "contents"
    contents = open(file_path).read()

    # return contents of your file as one long string
    return contents

def make_chains(text_string):
    """
    
    Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'juanita'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

    """

    # split text string into a list of words
    words = text_string.split()

    # create dictionary
    chains = {}

    # iterate over the index numbers of the list
    for i in range(len(words)-2):
        
        # create a tuple of two n-grams
        bigrams = (words[i], words[i+1])

        # check for repeat of keys / bigrams
        if bigrams not in chains:

            # if the key doesn't exists, add key to chains
            chains[bigrams] = [words[i+2]]

       # if bigram is in the list, append value to the type list
        else:
            chains[bigrams].append(words[i+2])

    # import pprint
    # pprint.pprint(chains)
    return chains

def make_text(chains):
    """
    Returns text from chains.
    """

    words = []

    # Set random tuple to variable key
    key = choice(chains.keys())


    # First time through key in chains, unpack X - a tuple - to get  
    # key[0], key[1]  = key
    # print key0]
    # print key[2]
    # Append key[0], key[1] to words

    words.append(key[0])
    words.append(key[1])

    # while tuple is a key in chains, keep looping 
    while key in chains:

        # Randomly choose a value from chains
        word = choice(chains[key])

        # Append word to words
        words.append(word)

        key = (key[1], word)

    return " ".join(words)

# assigns greens-eggs.txt to variable
input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# print chains       <-- do this to test a portion of this exercise

# Produce random text
random_text = make_text(chains)

print random_text

# Achievement unlocked! Code reviewed by Leslie and Agne. Is working!"