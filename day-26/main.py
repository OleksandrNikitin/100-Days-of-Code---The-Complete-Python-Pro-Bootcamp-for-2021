import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ")

list_of_the_phonetic_codes = [phonetic_dict[letter.upper()] for letter in user_input]

print(list_of_the_phonetic_codes)
