import random
import string

def random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))