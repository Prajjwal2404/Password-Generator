import random

def random_password(length):
    password = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$%^&*+'
    for _ in range(length):
        password += random.choice(characters)
    return f"Password: {password}"
