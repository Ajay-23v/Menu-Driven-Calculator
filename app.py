def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def menu():
    print("\n--- Calculator Menu ---")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice = input("Enter choice (1-5): ")
    if choice == '5': return False
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1': print("Result:", add(num1, num2))
        elif choice == '2': print("Result:", subtract(num1, num2))
        elif choice == '3': print("Result:", multiply(num1, num2))
        elif choice == '4': print("Result:", divide(num1, num2))
        else: print("Invalid Choice")
    except ValueError:
        print("Please enter valid numbers.")
    return True

if __name__ == "__main__":
    menu()
