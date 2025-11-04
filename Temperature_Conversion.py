def C_to_F(temp):
    converted_temp=1.8*temp+32
    return converted_temp
def F_to_C(temp):
    converted_temp=(5/9)*(temp-32)
    return converted_temp

temp=float(input("Enter temperature you'd like to convert:"))
unit1=input("Enter unit of temperature that you entered (C or F):")
unit2=input("Enter the unit you would like to convert too (C or F):")

if unit1.lower()=="c" and unit2.lower()=="f":
    print(f"Temperature in Fahrenheit is:{C_to_F(temp)}")

elif unit1.lower()=="f" and unit2.lower()=="c":
    print(f"Temperature in Celsius is:{F_to_C(temp)}")

else:
    print("Invalid operation")