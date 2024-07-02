def calc():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    print("\nOperations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    operation = input("Choose an operation (1-4): ")
    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation selected! Please choose from 1-4.")
def main():
    print("Calculator")
    while True:
        calc()
        answer = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if answer != 'y':
            print("Exiting Application!")
            break
if __name__ == "__main__":
    main()