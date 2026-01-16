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
print(spaces)

total_sum = 0
for i in range(100):
    total_sum = total_sum + (i + 1)
print(total_sum)
print(spaces)

for i in range(100):
    words = input("Just input random words (q to quit): ")
    if words.lower() == "q":
        break
    print(f"{words}")
print(spaces)

blocks = "[]"
rows = 5
columns = 2
for i in range(rows):
    print(blocks, end="")
    for j in range(columns - 1):
        print(blocks, end="")
    print()
print(spaces)
    
for i in range(rows):
    print(blocks, end="")
    for j in range(i):
        print(blocks, end="")
    print()
print(spaces)

for i in reversed(range(rows)):
    print(blocks, end="")
    for j in range(i):
        print(blocks, end="")
    print()
print(spaces)

name = input("Your name: ")
for i in range(len(name)):
    print(i, name[i])
print(spaces)

print('Password to pass is "Felixcute123"')
for i in range(100):
    password = input("Insert password: ")
    if password == "Felixcute123":
        break
print(spaces)

for i in range(1, 20, 3):
    if i == 4:
        continue    #for extra credits! uwu
    if i == 16:
        break
    print(i)