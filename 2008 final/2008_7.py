def add(one,two):
    return(one+two)
def subtract(one,two):
    return(one-two)
def multiply(one,two):
    return(one*two)
def divide(one,two):
    return(one/two)
def modulus(one,two):
    return(one%two)

choice = input("Enter(add/subtract/multiply/divide/modulus):")
one = float(input("first number = "))
two = float(input("second number = "))

if choice == "add":
    print("The result of add is",round(add(one,two),2))
elif choice == "subtract":
    print("The result of subtract is", round(subtract(one,two),2))
elif choice == "multiply":
    print("The result of multiply is", round(multiply(one,two),2))
elif choice == "divide":
    print("The result of divide is", round(divide(one,two),2))
elif choice == "modulus":
    print("The result of modulus is", round(modulus(one,two),2),"%")
else:
    print("can't calculate plz go to photomath")
