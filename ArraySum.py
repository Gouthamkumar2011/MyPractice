# creating an empty list
lst = []
total = 0
# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    lst.append(ele)  # adding the element
    for j in range (0,len(lst)):
        total = total + lst[j]

print("The sum of elements in list", total)
print(lst)
