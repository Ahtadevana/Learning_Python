#Covering the basic concepts of list, sets, and tuples
spaces = "-----"
fruits = ["Durian", "Lychee", "Rambutan", "Apple"]

print(fruits[::-1])             #you can also use string indexing to navigate through lists
print(spaces)

for fruit in fruits:            #instead of naming i as "for i in range()" use its singular from its plural name
    print(fruit)
print(spaces)

print(dir(fruits))              #prints the list's attributes
#help(fruits)                   #i won't print this but in case i need help, i can print this function
print(spaces)

print(len(fruits))              #return the total of index within a list
print(spaces)

print("Apple" in fruits)        #returns the value of a boolean
print(spaces)

fruits[0] = "Tomato"            #reassigning a value within a list using index
print(fruits[0])
print(spaces)

fruits.append("Salmonberry")    #adding another value to the list using .append()
fruits.remove("Lychee")         #removes lychee from index 2 within the fruits list
fruits.insert(2, "Lychee")      #adds lychee back to its original index
print(fruits)
print(spaces)

fruits.sort()                   #sorting list alphabetically
fruits.reverse()                #reverse the order of the list (not alphabetically!)
print(fruits)
print(spaces)

print(fruits.index("Lychee"))   #shows the index of a certain value inside a list
print(spaces)

fruits.insert(0, "Apple")
print(fruits.count("Apple"))    #counts how many value is within one list (output: 2)
print(spaces)

fruits.clear()                  #removes the entire list
print(spaces)

#sets, you can add / remove, but you cant change the values and you cant duplicate it
vegetables = {"Broccoli", "Mushrooms", "Cauliflower"}   #unordered, unorganized (places are randomized)
print(vegetables)
print(spaces)

#tuples, ordered and unchangeable, you can duplicate it and it's way faster
planets = ("Mercury", "Venus", "Earth", "Mars")
print(planets)
print(spaces)