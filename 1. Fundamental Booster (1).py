print("Welcome to Interactive Personal Data Collector !")

name = str(input("\nPlease enter your name : "))
age = int(input("Please enter your age : "))
height = float(input("Please enter your height in meter : "))
faourite_number = int(input("Please enter your faourite number : "))

print("\n\nThank you !  Here is the information we collected : ")

print("\n\nName :" , name , "( Type :" , type(name) , ", Memory Address :" , id(name) , ")")
print("Age :" , age , "( Type :" , type(age) , ", Memory Address :" , id(age) , ")")
print("Height :" , height , "( Type :" , type(height) , ", Memory Address :" , id(height) , ")")
print("Faourite Number :" , faourite_number , "( Type :" , type(faourite_number) , ", Memory Address :" , id(faourite_number) , ")")

print("\n\nYour birth year is approximately :" , 2025 - age , "( based on your" , age , ")")

print("\n\nThank you for using Personal Data Collector. Goodbye !")