#Written by Charlie Sober


def encoder(password):
    password_str = str(password)
    result = ""
    for char in password_str:
        new_digit = (int(char) + 3) % 10
        result += str(new_digit)
    return result

org_psswrd = input("Please enter your password: ")
print(encoder(org_psswrd))
