import string, random, time

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(characters)
        print(password, end='\r')  # Update on the same line
    return password

length = int(input("Enter the password length: "))
print("\nGenerated Password:", generate_password(length))
