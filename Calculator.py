print("Welcome! Please follow the instruction for using Calculator")
num1 = float(input("Enter the first number: "))
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiple (*)")
print("4. Divide (/)")
choice = input("Enter the choice by using Number: ")
num2 = float(input("Enter the second number: "))
print("Here is your answer")

if choice == '1':
    print(f"{num1} + {num2} = {num1 + num2}")
    print("Thank You for Using Calculator")
elif choice == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
    print("Thank You for Using Calculator")
elif choice == '3':
    print(f"{num1} * {num2} = {num1 * num2}")
    print("Thank You for Using Calculator")
elif choice == '4':
        print(f"{num1} / {num2} = {num1 / num2}")
        print("Thank You for Using Calculator")
else:
        print("Invalid input")
        
