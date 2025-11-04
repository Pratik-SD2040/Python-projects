strings=input("please enter your string:")
list_str=strings.split()
reversed_list=[]
while len(list_str)!=0:
      g=list_str.pop()
      reversed_list.append(g)
print(' '.join(reversed_list))