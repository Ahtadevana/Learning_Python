#Typecasting -> Turning a variable type for a different type (ex. float -> int, int -> str, etc)

#Integer -> String
age = 10
age = str(age)

#Float -> integer
gpa = 3.41
gpa = int(gpa)

#Accepting user input
name = bool(input("Input your name: "))

#Checking whether variable 'name' is already "Filled"
if name == False:
    print("You didn't input your name!")
else:
    print("Acces granted: ")
    print(type(age))    #type() function used to show what type of var it is
    print(type(gpa))    
    print(type(name))