#Problem 1
Week_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
Sale_list=[50,75,150,125,100]

max_sale = Sale_list[0]
max_index = 0

for i in range(1, len(Sale_list)):
    if Sale_list[i] > max_sale:
        max_sale, max_index = Sale_list[i], i

print("The max sales are:$",max_sale)
print("The max sales day is:",Week_list[max_index])

#Problem 2
numbers=[]

number=int(input("Enter value (or 0 to end):  "))
while number!=0:
    numbers.append(number)
    number=int(input("Enter value (or 0 to end):  "))

print("Value:   ",numbers)

highest=max(numbers)
lowest=min(numbers)
range=highest-lowest
print("Highest:",highest)
print("Lowest:",lowest)

