menu={"popcorn":60,"burgers":50,"pizza":120,"maggie":40,"coffee":30,"tea":10}
print(f"here is the menu\n{menu}\nwhat would you like to have?")
item=[]
prices=[]
while True:
    item.append(input("Your order?[type done to get total]\n"))
    print(item)
    if item[-1]=="done":
        item.remove("done")
        break
for i in item:
    prices.append(menu.get(i))
print(f"Your total is {sum(prices)}")