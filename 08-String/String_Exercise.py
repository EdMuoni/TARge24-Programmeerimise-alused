"""Sõnede funktsioonid"""

first_name = "James"
last_name = "Bond"
full_name = first_name + " " + last_name
self_description_sentence = f"My name is {last_name}, {first_name} {last_name}."

cake = "vahukoormarjatäidispõhi"
print("vahukoor\nmarjad\ntäidis\npõhi")

# Loo muutuja original_string
original_string = "Programming is fun!"
# Loo muutuja backwards tagurpidi sõne jaoks
backwards = original_string[::-1]
# Loo muutuja every_other, mis võtab iga teise tähe
every_other = original_string[::2]
# Loo muutuja first_word_reversed, mis võtab esimese sõna tagurpidi
first_word_reversed = original_string.split()[0][::-1]
