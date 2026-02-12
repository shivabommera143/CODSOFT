import random
import string
print("===== PASSWORD GENERATOR =====")
length = int(input("Enter desired password length: "))
print("\nChoose password complexity:")
print("1. Letters only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")
choice = input("Enter choice (1/2/3): ")
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
if choice == '1':
    characters = letters
elif choice == '2':
    characters = letters + numbers
elif choice == '3':
    characters = letters + numbers + symbols
else:
    print("Invalid choice! Defaulting to Letters only.")
    characters = letters
password = ""
for i in range(length):
    password += random.choice(characters)
print("\nGenerated Password:")
print(password)
 
