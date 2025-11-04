str1=input("enter your string:")

print(list(set(filter(lambda ch:ch in "aeiou",str1.lower()))))