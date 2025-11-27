import random
import string
def generate_password(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    all_chars = lowercase + uppercase + digits
    for _ in range(length - len(password_chars)):
        password_chars.append(random.choice(all_chars))
    random.shuffle(password_chars)
    password = ''.join(password_chars)
    return password
if __name__ == "__main__":
    while True:
        pwd = generate_password(12)
        print("Password:", pwd)
        choice = input('Type "new" for a new password or "q" to quit: ').strip().lower()
        if choice != "new":
            break
