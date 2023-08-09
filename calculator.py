
def exponentiate(x, y):
    return x ** y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        try:
            print("Result:", divide(num1, num2))
        except ValueError as e:
            print("Error:", str(e))
    elif choice == '5';
        print("Result:", exponentiate(num1, num2))
    else:
        print("Invalid input. Please select a valid operation (1/2/3/4).")

if __name__ == "__main__":
    calculator()
