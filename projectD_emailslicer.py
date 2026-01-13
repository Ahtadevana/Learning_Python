#Making an email slicer program using string indexing

email = input("Insert your email: ")

if "@" in email:    #if the character symbol @ is in var email, run this:
    slicer = email.index("@")
    print("Your username is " + email[:slicer])
    print("Your domain is " + email[slicer + 1:])
else:
    print("Email must contain '@'!")