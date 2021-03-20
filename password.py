import argparse
import random
import pyperclip
# create lists
list_symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lowercase_list = ["a", "b", "c", "v", "q", "u", "x", "p", "q", "y"]

uppercase_list = ["A", "B", "S", "C", "T", "W", "R", "M", "N", "J"]

# create a join to join the 4 lists together
password_character_bank = list_symbols + list_num + lowercase_list + uppercase_list

# Create list WITHOUT symbols
password_character_bank_no_symbols = list_num + lowercase_list + uppercase_list

password = []
password_length = int(input("How many characters would you like your password? "))
use_symbols = (input("Would you like to use symbols? "))

# Use IF statement to determine a password with or without special characters
if use_symbols == "yes":
    # loop over password character bank and choose a character at random
    for x in range(password_length):
        password.append(random.choice(password_character_bank))

    # else choose a password without special characters
else:
    for x in range(password_length):
        password.append(random.choice(password_character_bank_no_symbols))

# print random password to user
print(password)
pyperclip.copy(password)
