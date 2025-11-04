#filter students having marks greater than or equal to 80


data = {
    'Nitesh': 78,
    'Rahul': 98,
    'Raj': 91,
    'Amar': 90,
    'Abhi': 81,
    'Simran': 73,
    'Kunal': 67,
    'Sneha': 88
}
def sorter(stds):
    return data[stds]>=80
print(list(filter(sorter,data)))
print(list(filter(lambda key: data[key]>=80,data)))