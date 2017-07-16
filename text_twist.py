import os
from operator import itemgetter

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    "Return a pair of sets: all the words in a file, and all the prefixes"
    file = open(filename)
    text = file.read().upper()
    wordset = set(word for word in text.splitlines())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist(os.path.expanduser("~/downloads/wordsEn/wordsEn.txt"))

def find_words(letters, pre='', results=None):
    "Find all words that can be made from the letters in hand."
    if results is None: results = set()
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            find_words(letters.replace(L,'',1), pre+L, results)
    return results

def alphabetical(letters):
    new_set = find_words(letters)
    new_list = list(new_set)
    maximum = sorted(new_list).reverse()    
    return maximum

def biggest_word(letters):    
    new_set = find_words(letters)
    new_list = list(new_set)
    return sorted(new_list, key=len, reverse=True)

def count_words(s, n):
    """Count the number of occurences of each word in s. Sort the occurences
    in descending order (alphabetically in case of ties). Return the top n
    words as a list of tuples (<word>, <count>)  
    Return the n most frequently occuring words in s."""
    p = [(e,s.split().count(e)) for e in s.split()]
    q = sorted(set([(x,y) for (x,y) in p]),key=lambda (x,y):(abs(y)),reverse=True)
    r = sorted(q, key=itemgetter(0))
    return sorted(r, key=itemgetter(1), reverse=True)[0:n]



def test_count_words():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)

#print alphabetical("DAFEAFC")
print test_count_words() 

print biggest_word('EPGTSU')

