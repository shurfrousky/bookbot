def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # showing user amount of words in the book
    word_count = String_Word_Count(file_contents)
    print(f"{word_count} Words in this book.")
    print("-----------------------------------------------")

    char_count = Char_Count(file_contents)
    print(f"Amount of characters in this book: \n{char_count}")

# converts book txt to strings, returns number of words in string
def String_Word_Count(book_contents):
    words = book_contents.split()  # convert txt to one big list of strings
    num_of_words = 0

    for word in words:  # adding up the amount of words from 'words' string list
        num_of_words += 1
    
    return num_of_words

# adds up all char and put into a dict
def Char_Count(book_contents2):
    words_low = book_contents2.lower() # lowercasing all the txt
    char_amount = {} # dict to store chars from book txt

    for word in words_low:
        char_amount.setdefault(word, 0) # initializing dict, checking keys, keeping them unique
        char_amount[word] += 1 # incrememnting key value's

    return char_amount

main()