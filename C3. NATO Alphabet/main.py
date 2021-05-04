import pandas


# Create dictionary from csv
data_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in data_alphabet.iterrows()}

# Convert input to alphabet
question = input("Enter a word: ").upper()
word_list = ' '.join([alphabet[letter] for letter in question if letter != " "])
print(word_list)
