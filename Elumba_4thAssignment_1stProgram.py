# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

def AllInputs():
    namef = input("Enter your name: ")
    agef = int(input("Enter your age: "))
    addressf = input("Enter your address: ")
    return namef, agef, addressf

def displayOutput(namef, agef, addressf):
    print(f"Hi, my name is {namef}. I am {agef} years old and I live in {addressf}.")

name, age, address = AllInputs()
displayOutput(name, age, address)