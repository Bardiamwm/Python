import random, string, time
word = input("enter word: ")
password = ""
i = 0
while password != word:
    password = password[:i] + (string.ascii_letters + string.digits + "_ ")[random.randint(0, 63)]
    if password[i] == word[i]:
        i += 1
    print(password)
    time.sleep(0.02)