#show laptops according to user's budget
budget=float(input("Enter your budget here:"))
laptops={"hp":50000,"lenovo":60000,"asus":80000,"mac":120000}
def budget_fxn(money):
    return True if laptops[money]<=budget else False
g=filter(budget_fxn,laptops)
print(list(g))