import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {word.letter: word.code for (index, word) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# dict = pandas.DataFrame(new_dict)
word = input("Enter the word : ").upper()
new_list = [new_dict[letter] for letter in word]
print(new_list)
