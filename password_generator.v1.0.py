import random

print("=== Password Generator v1.0 ===")

while True:
    try:
        length = int(input("\nHow many characters do you want? (8-20): "))
        if length < 8 or length > 20:
            print("Only 8 to 20! Security Purposes")
            continue
        
        letters_small = "abcdefghijklmnopqrstuvwxyz"
        letters_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&*"
        
        all_chars = letters_small + letters_big + numbers + symbols
        
        password = ""
        
        for i in range(length):
            random_char = random.choice(all_chars)
            password = password+ random_char
        
        print("_" * 30)
        print(f"Generated Password: {password}")
        print(f"Length: {len(password)} characters")
        print("_" * 30)
        
        again = input("Do it again? (y/n): ")
        if again.lower() != 'y' :
            print("Thank you! Don't forget your password.")
            break
        
    except:
        print("Just enter the number! 8-20")