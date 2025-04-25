def is_valid_password(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False
    return True


def create_password():
    print("Create Your Bank Account Password")
    password = input("Enter your password: ")

    if is_valid_password(password):
        print("Password is valid. Account setup completed!")
    else:
        print("Please try again with a valid password.")
