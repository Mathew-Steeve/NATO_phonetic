import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {word.letter: word.code for (index, word) in data.iterrows()}
# while KeyError:


def generate():
    word = input("Enter the word : ").upper()
    try:
        new_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please. ")
        generate()
    else:
        print(new_list)
        # break


generate()
