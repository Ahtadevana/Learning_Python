#i want ot better understand how for loops work
#and here i can make a bunch of for loop algorithms
spaces = "-------"
number = 5

for i in range(10):
    print(i+ 1) #count i, output: 1 -> 10
print(spaces)

for i in reversed(range(10)):
    print(i+ 1)    #count i in reverse output: 10 -> 1
print(spaces)

for i in range(5):
    print("OwO")
print(spaces)

for i in range(10):
    i += 1
    result = number * i
    print(f"{number} x {i} = {result}")

result = 0
for i in range(100):
    result = result + (i + 1)
print(result)