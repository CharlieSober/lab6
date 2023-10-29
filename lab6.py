#Written by Charlie Sober

def encode(password):
    password_str = str(password)
    result = ""
    for char in password_str:
        new_digit = (int(char) + 3) % 10
        result += str(new_digit)
    return result


continue_app = True


while continue_app:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("3. Quit")
    print()
    option = int(input("Please enter an option: "))
    if option == 1:
        og_psswrd = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored")
        encoded_psswrd = encode(og_psswrd)
    if option == 3:
        continue_app = False
