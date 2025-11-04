Items=[]
prices=[]
quiting=""
count=0
while quiting!="n":
    item=input("Please enter your items in this list:")
    Items.append(item)
    print("Is there anything else that you'd like to add?\nType N to quite or keep adding")
    quiting=input()
    quiting.lower()
    print(Items)
while len(prices)!=len(Items):
    price=int(input(f"How much was {Items[count]}"))
    prices.append(price)
    count+=1
    print(dict(zip(Items,prices)))
print(f"your total billing amount comes out to be:{sum(prices)}")
