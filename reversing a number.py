ans = ""
while ans != "y":
    number = input("Enter your number: ")
    reversed_number = number[::-1]
    print(reversed_number)
    ans = input("Do you wanna quit? (y/n): ")
