# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

alphabet_data_frame = pandas.read_csv("./nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for index,row in alphabet_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()

nato_format = [alphabet_dict[letter] for letter in user_input]

print(nato_format)
