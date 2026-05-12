import os
from datetime import datetime

# File paths for Storage
BALANCE_FILE = "/storage/emulated/0/savings.txt"
HISTORY_FILE = "/storage/emulated/0/savings_history.txt"

def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, 'r') as f:
            try:
                return float(f.read())
            except:
                return 0.0
    return 0.0
    
def save_balance(amount):
    with open(BALANCE_FILE, 'w') as f:
        f.write(str(amount))
        
def add_history(action, amount, balance):
    timestamp = datetime.now().strftime("%m/%d %I:%M%p")
    with open(HISTORY_FILE, 'a') as f:
        f.write(f"{timestamp} | {action} ₱{amount: .2f} | Balance: ₱{balance: .2f}\n")
        
def show_history():
    print("\nLAST 5 TRANSACTION")
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            lines = f.readlines()
            if lines:
                for line in lines[-5:]:
                    print(line.strip())
            else:
                print("No history yet")
    else:
        print("No histroy yet")
        
while True:
    balance = load_balance()
    
    print("\n" + "="*30)
    print("SAVINGS TRACKER")
    print("="*30)
    print(f"CURRENT BALANCE: ₱{balance: .2f}")
    print("="*30)
    print("1. Deposit - Add amount")
    print("2. Withdraw - Take amount")
    print("3. History - View transactions")
    print("4. Reset - Clear all savings")
    print("5. Exit")
    print("="*30)
    
    choice = input("Choose 1-5: ")
    
    if choice == '1':
        try:
            amount = float(input("Enter deposit amount: ₱"))
            if amount > 0:
                new_balance = balance + amount
                save_balance(new_balance)
                add_history("DEPOSIT", amount, new_balance)
                print(f"\nDeposited ₱{amount: .2f}")
                print(f"New balance: ₱{new_balance: .2f}")
            else:
                print("\nAmount must be greater than 0")
        except:
            print("\nPlease enter a valid number")
            
    elif choice == '2':
        try:
            amount = float(input("Enter withdraw amount: ₱"))
            if 0 < amount <= balance:
                new_balance = balance - amount
                save_balance(new_balance)
                add_history("WITHDRAW", amount, new_balance)
                print(f"\nWithdraw ₱{amount: .2f}")
                print(f"New Balance: ₱{new_balance: .2f}")
            elif amount > balance:
                print(f"\nInsufficient funds. You only have ₱{balance: .2f}")
            else:
                print("\nAmount must be greater than 0")
        except:
            print("\nPlease enter a valid number")
    
    elif choice == '3':
        show_history()
        
    elif choice == '4':
        confirm = input("Reset all savings? Type YES to confirm: ").upper()
        if confirm == "YES":
            save_balance(0.0)
            add_history("RESET   ", balance, 0.0)
            print("\nBalance reset to ₱0.00")
        else:
            print("\nCancelled")
            
    elif choice == '5':
        print(f"\nGoodbye! Final balance: ₱{balance: .2f}")
        print("Your data is saved on yout phone")
        break
        
    else:
        print("\nPlease choose 1-5 only")#