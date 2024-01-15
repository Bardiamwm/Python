import random, string
password = ""
while len(password) != 12:
    password += (string.ascii_letters + string.digits + "_")[random.randint(0, 62)]
print("your password is:", password)