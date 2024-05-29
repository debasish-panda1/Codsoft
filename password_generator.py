import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("WELCOME TO PASSWORD GENERATOR!!")
n_letters = int(input("Enter the number of letters you want in your password: "))
n_numbers = int(input("Enter the number of numbers you want in your password: "))
n_symbols = int(input("Enter the number of symbols you want in your password: "))

password_list = []

for _ in range(n_letters):
    char = random.choice(letters)
    password_list.append(char)

for _ in range(n_numbers):
    char = random.choice(numbers)
    password_list.append(char)

for _ in range(n_symbols):
    char = random.choice(symbols)
    password_list.append(char)

random.shuffle(password_list)
password = "".join(password_list)

print("Generated Password:", password)
