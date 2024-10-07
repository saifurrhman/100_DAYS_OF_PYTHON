password = ""
for _ in range(nr_letters):
    password += random.choice(letters)
for _ in range(nr_numbers):
    password += random.choice(numbers)
for _ in range(nr_symbols):
    password += random.choice(symbols)
print(f"Your password is: {password}")