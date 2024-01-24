def print_upper_words(words):

    '''Print each word in upper case'''

    for data in words:
        data = data.upper()
        print (f'''{data}''')

print_upper_words(['hat', 'dog'])        

def print_upper_words2(words):

    '''Print word with starting letter e'''
    for data in words:
        if data.startswith ('e') or data.startswith ('E'):
            print(data)
    

print_upper_words2(['eat', 'dog'])      


def print_upper_words3(words, start_with):

    '''Print word with starting letter user provided letter'''

    for data in words:
        for letter in start_with:
            if data.startswith(letter):
                print(data)

print_upper_words3(["hello", "hey", "goodbye", "yo", "yes", 'prav'], start_with={"h", "y"})
