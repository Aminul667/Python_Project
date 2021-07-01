import random
import string

def get_random_password(length):
    # choose from all lowercase Upper case letter, digits and symbols
    digits = string.digits
    symbols = string.punctuation
    letters = string.ascii_letters

    # list of available characters
    password_symbols = digits + letters + symbols

    result_str = ''.join(random.choice(password_symbols) for i in range(length))

    print(result_str)

length = int(input("Enter Password Length: "))

get_random_password(length)