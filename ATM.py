# ATM MACHINE

account_data = []
print("Welcome to SK the ATM!")
while True:
    print("\nATM Operations:")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Update Account")
    print("6. Display All Accounts")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":  # Create Account
        account_holder_name = input("Enter account holder name: ")
        account_number = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))
        pin = input("Enter PIN: ")
        account_info = {'account_holder_name': account_holder_name, 'account_number': account_number,
                        'balance': initial_balance, 'pin': pin}
        account_data.append(account_info)
        print(f"Account for {account_holder_name} created successfully.")
    elif choice == "2":  # Check Balance
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        account_found = False
        for account in account_data:
            if account['account_number'] == account_number and account['pin'] == pin:
                print(f"Account Balance for {account['account_holder_name']}: ${account['balance']}")
                account_found = True
                break
        if not account_found:
            print("Account not found or incorrect PIN.")
    elif choice == "3":  # Deposit Money
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        amount = float(input("Enter deposit amount: "))
        account_found = False
        for account in account_data:
            if account['account_number'] == account_number and account['pin'] == pin:
                account['balance'] += amount
                print(f"Deposit successful. New balance: ${account['balance']}")
                account_found = True
                break
        if not account_found:
            print("Account not found or incorrect PIN.")
    elif choice == "4":  # Withdraw Money
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        amount = float(input("Enter withdrawal amount: "))
        account_found = False
        for account in account_data:
            if account['account_number'] == account_number and account['pin'] == pin:
                if account['balance'] >= amount:
                    account['balance'] -= amount
                    print(f"Withdrawal successful. New balance: ${account['balance']}")
                else:
                    print("Insufficient funds.")
                account_found = True
                break
        if not account_found:
            print("Account not found or incorrect PIN.")
    elif choice == "5":  # Update Account
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        account_found = False
        for account in account_data:
            if account['account_number'] == account_number and account['pin'] == pin:
                new_name = input("Enter new account holder name: ")
                new_pin = input("Enter new PIN: ")
                account['account_holder_name'] = new_name
                account['pin'] = new_pin
                print(f"Account information updated successfully.")
                account_found = True
                break
        if not account_found:
            print("Account not found or incorrect PIN.")
    elif choice == "6":  # Display All Accounts
        if len(account_data) > 0:
            print("All Accounts:")
            for account in account_data:
                print(f"Account Holder: {account['account_holder_name']}, Account Number: {account['account_number']}, Balance: ${account['balance']}")
        else:
            print("No accounts found.")
    elif choice == "7":  # Exit
        print("Thank you for using the ATM!")
        print("Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
