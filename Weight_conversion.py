def g_to_kg(weight_in_g):
    return f"{weight_in_g/1000}kg"

def kg_to_g(weight_in_kg):
    return f"{weight_in_kg*1000}g"

weight=float(input("enter your weight"))
unit1=input("enter unit of your weight (kg or g):")
unit2=input("enter unit to which you would like to convert:")

if unit1=="g" and unit2=="kg":
    print(f"your weight in kg:{g_to_kg(weight)}")
elif unit1=="kg" and unit2=="g":
    print(f"your weight in g:{kg_to_g(weight)}")
else:
    print("invalid data entered")