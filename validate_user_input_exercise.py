
print("Please read below instructions carefully before entering your password\nIt should be no more that 12 characters\nIt should not contain spaces\nIt should not contain digits")
user_input=input("Please enter your password:")

if len(user_input)<=12 and user_input.isalpha():
    print(f"{user_input} is accepted")
else:
    print(f"{user_input} is invalid.\nplease try again")
