def password_generator():
    import string
    import random
    letter = string.ascii_letters
    digit = string.digits
    symbols = "!@#$%^&*_-/"
    all_char = letter+digit+symbols
    
    length = int(input("Enter your password length: " ))
    generator = "".join(random.choice(all_char)for _ in range(length))
    print("Your Generated password is here: ", generator)
    
password_generator()
print("Done")
