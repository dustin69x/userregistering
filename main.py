# Registering

reg_username = input("Please Enter the username that you want to  register with: ")
reg_password = input("please Enter the password that you want to register with: ")

# Drama
print("Please wait while we register you")

# logging in
print("Okay we're done Please Enter your username and password")
log_user = input("Username: ")
log_pass = input("password: ")
# Checking if username and password are the same as the one registered with
if log_user == reg_username and log_pass == reg_password:
    print("Congratulation you're in! ")
else:
    print("Invalid username or password")


