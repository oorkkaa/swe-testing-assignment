from calculator_logic import add, subtract, multiply, divide

def process_operation(num1, op, num2):
    match op:
        case '+': return add(num1, num2)
        case '-': return subtract(num1, num2)
        case '*': return multiply(num1, num2)
        case '/': return divide(num1, num2)
        case _: return "Error"


def main():
    print("calculator app by Orkhan Sultanov 231ADB131")

    while True:
        try: #input collection
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        print(f"\nYou entered: {num1} {op} {num2}")
        decision = input("Type 'C' to clear, or press Enter to proceed: ").upper() #implementation of input clearing

        if decision == 'C':
            continue

        match op: #calculations
            case '+': result = add(num1, num2)
            case '-': result = subtract(num1, num2)
            case '*': result = multiply(num1, num2)
            case '/': result = divide(num1, num2)
            case _:
                result = "Error: Invalid operator"
                print(result)
                continue

        print(f"Result: {result}")

        #option to quit application
        choice = input("\nType 'Q' to quit, or type any other key to continue: ").upper()
        if choice == 'Q':
            break
        else:
            print("\n")
            continue

if __name__ == "__main__":
    main()