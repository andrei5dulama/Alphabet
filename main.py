student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data_file = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter:row.code for (index, row) in data_file.iterrows()}
print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = [letter for letter in input("Enter your name: ").upper()]
    try:
        phonetic_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters in the Alphabet please")
        generate_phonetic()
    else:
        print(phonetic_list)
generate_phonetic()