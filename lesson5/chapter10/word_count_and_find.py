def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
def find_words(filename, search):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        contents = contents.lower()
        search = search.lower()
        words = contents.count(search)
        print(f"The file {filename} has {words} instances of '{search}'.")

filenames = ['lesson5/chapter10/jabberwocky.txt', 'lesson5/chapter10/iSawAPeacock.txt', 'lesson5/chapter10/heyDiddleDiddle.txt',]
for filename in filenames:
    count_words(filename)
word = input("What word would you like to search for? ")
for filename in filenames:
    find_words(filename, word)