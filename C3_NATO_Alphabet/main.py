import pandas


# Create dictionary from csv
data_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in data_alphabet.iterrows()}
1231
# Convert input to alphabet

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        word_list = [alphabet[letter] for letter in word]
    except KeyError:
        print("The word must only contain letters in the alphabet.")
        generate_phonetic()
    else:
        print(word_list)
        
        
    
generate_phonetic()

