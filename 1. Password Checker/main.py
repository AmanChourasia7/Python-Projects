username = input("Enter Username:  ")
password = input("Enter Password:  ")

password_length = len(password)

hidden_password = "*" * password_length

print(f"Greetings {username}, your passsword ({hidden_password}), is {password_length} characters long.")
