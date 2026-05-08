def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y
    
def main():
    while True:
        print("\n=== CALCULATOR===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Choose 1-5: ")
        
        if choice == "5":
            print("Goodbye! Thanks for using Calculator ")
            break
        
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == "1":
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("Invalid input! Numbers only please.")
        else:
            print("Invalid choice! Pick 1-5 only.")
if __name__ == "__main__":
    main()
    
# Jhon Nexter A. Herrada
# May 8, 2026 Friday
# calculator.py
# Wanting to be a successful for myself and family <3
# Grade 11