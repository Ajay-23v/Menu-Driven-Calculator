def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def menu():
    print("\n Calculator Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    if choice == '3':
        return False
        
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(r"Result:", add(num1, num2))
    elif choice == '2':
        print(r"Result:", subtract(num1, num2))
    else:
        print("Invalid Choice")
    return True

if __name__ == "__main__":
    
    menu()
