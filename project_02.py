"""Password Check"""
# Sindri Snær Gunnarsson
# 14-02-22
# Program that checks if passwords from user meet safety requirements

SYMBOLS = '!#$%&?~*+-/='
LOWER_LIMIT = 8
UPPER_LIMIT = 30
REQUIRED_CONDITIONS = 4


def correct_password_length(password):
    """Checks if the password meets length requirement
    and returns boolean"""
    return LOWER_LIMIT <= len(password) <= UPPER_LIMIT


def contains_upper_case(password):
    """Checks if password has upper case character
    and returns boolean"""
    for i in password:
        if i.isupper():
            return True
    return False


def contains_lower_case(password):
    """Checks if password has lower case character
    and returns boolean"""
    for i in password:
        if i.islower():
            return True
    return False


def contains_number(password):
    """Checks if password has a number
    and returns boolean"""
    for i in password:
        if i.isdigit():
            return True
    return False


def contains_space(password):
    """Checks if password has a space
    and returns boolean"""
    for i in password:
        if i == ' ':
            return True
    return False


def contains_symbols(password):
    """Checks if password contains required symbol
    and returns boolean"""
    for i in password:
        for j in SYMBOLS:
            if i == j:
                return True
    return False


def conditions_met(password):
    """Checks if the password fulfills 4 out of 5
    requirements and returns boolean"""
    conditions = [contains_upper_case(password), contains_lower_case(password),
                  contains_space(password), contains_number(password), contains_symbols(password)]
    return sum(conditions) >= REQUIRED_CONDITIONS


def print_missing_requirements(password):
    """Prints the text for an invalid password or length
    and what requirements of the password are missing"""
    repeated_string = 'The password does not contain '
    if not correct_password_length(password):
        print('Invalid length')
    else:
        print('Missing requirements:')
        if not contains_upper_case(password):
            print(repeated_string + 'an upper case letter')
        if not contains_lower_case(password):
            print(repeated_string + 'an lower case letter')
        if not contains_number(password):
            print(repeated_string + 'a digit')
        if not contains_space(password):
            print(repeated_string + 'a space')
        if not contains_symbols(password):
            print(repeated_string + 'a symbol')


# ------------ Main Section ---------------
def main():
    valid_attempts = invalid_attempts = 0
    input_password = input('Password: ')

    while input_password.lower().strip() != 'q':
        if correct_password_length(input_password):
            if conditions_met(input_password):
                print(f'Valid password of length {len(input_password)}')
                valid_attempts += 1
            else:
                print_missing_requirements(input_password)
                invalid_attempts += 1
        else:
            print_missing_requirements(input_password)
            invalid_attempts += 1
        input_password = input('Password: ')

    print(f'You tried {valid_attempts + invalid_attempts} passwords,\
    {valid_attempts} valid, {invalid_attempts} invalid')


if __name__ == '__main__':
    main()
