correct_password = "12345"
attempts = 5

while attempts > 0:
    user_input = input("Enter the password: ")

    if user_input == correct_password:
        print("Password is correct, access allowed.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Password is incorrect. Attempts left:", attempts)
        else:
            print("Too many wrong attempts. Local authorities have been alerted!")