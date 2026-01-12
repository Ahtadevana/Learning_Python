#variables

#string
name = "Xervii"
password = "Hellyeah123"
print(f"namamu {name}, password: {password}") #Putting an f string to display the var's value

#integer
age = 18
print(f"umurmu: {age}")

#float
gpa = 3.41
print(f"IPKmu: {gpa}")

#boolean
is_student = False
is_online =  False

# if statement for testing the variable capabilities
if is_student:
    if is_online:
        print("In education, currently Online!")
    else:
        print("In education, currently Offline!")
elif not is_student:
    if is_online:
        print("Not in education, currently Online!")
    else:
        print("Not in education")
else:
    print("Invalid, denied entry!")