import random
import string
from english_words import get_english_words_set


def generate_secure_password():
    password_length = random.randint(8, 12)
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    if any(c.isupper() for c in password) \
            and any(c.islower() for c in password) \
            and any(c.isdigit() for c in password) \
            and any(c in string.punctuation for c in password) \
            and check_password(password):
        return password
    else:
        return generate_secure_password()


def check_password(password):
    for word in get_english_words_set(['web2'], lower=True):
        if word in password:
            return True
    return False


# Test the function
password = generate_secure_password()
print(password)
print(check_password(password))
