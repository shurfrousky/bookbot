def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # showing user amount of words in the book
    word_count = String_Word_Count(file_contents)
    print(f"{word_count} words in this book.")

    Char_Count(file_contents)

#converts book txt to strings, returns number of words in string
def String_Word_Count(book_contents):
    words = book_contents.split()  #convert txt to one big list of strings
    num_of_words = 0

    for word in words:  #adding up the amount of words from 'words' string list
        num_of_words += 1
    
    return num_of_words

def Char_Count(book_contents2):
    words_low = book_contents2.lower() #lowercasing all the txt
    words = words_low.split() # putting txt into 1 big string list
    char_amount = {'a': 0, 'b': 0, 'c': 0, 'd':  0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
                            'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0} #alphabatized dict

    for word in words:
        for char in word:
            if char in char_amount:
                char_amount[char] += 1

    print(char_amount)


main()