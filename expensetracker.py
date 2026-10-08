#START

#Ask the user for their name
name = input("What is your name? ")

#Ask the user how much money they have
money = float(input("How much money do you have? "))
print()

#Create a place to store expenses
expenses = []



while True:
    #Show the menu
    print("What would you like to do?")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. View Balance")
    print("5. Exit")
    #Get the user's choice
    choice = input("Please select an option: ")
    print()

    #IF the user chooses Add Expense:
    if choice == "1":
        #Ask for expense name
        expense_name = input("What is the expense name? ")
        #Ask for expense amount
        expense_amount = float(input("What is the expense amount? "))
        balance = money - sum(amount for _, amount in expenses)
        print()
        if expense_amount > 0 and expense_amount <= balance:
            #Save the expense
            expenses.append((expense_name, expense_amount))
            #Show success message
            print("Expense added successfully!")
            print()
        elif expense_amount <= 0:
            #Show error message
            print("Expense amount must be greater than zero.")
            print()
        else:
            #Show error message
            print("Insufficient funds for this expense.")
            print()

    #IF the user chooses View Expenses:
    elif choice == "2":
        if expenses:
            #Show all saved expenses
            for number, (expense_name, expense_amount) in enumerate(expenses, 1):
                print(f"{number}. {expense_name}: ₦{expense_amount:,.2f}")
            print()        
        else:
            print("No expenses recorded.")
            print()

    #IF the user chooses View Total:
    elif choice == "3":
        #Calculate all expenses
        total = sum(amount for _, amount in expenses)
        #Show total
        print(f"Total expenses: ₦{total:,.2f}")
        print()

    #IF the user chooses View Balance:
    elif choice == "4":
        #Calculate remaining money
        balance = money - sum(amount for _, amount in expenses)
        #Show balance
        print(f"Remaining balance: ₦{balance:,.2f}")
        print()

    #IF the user chooses Exit:
    elif choice == "5":
        #End the program
        print("Thank you for using the expense tracker!")
        break

    #Otherwise:
    else:
        #Tell the user the option is invalid
        print("Invalid option. Please try again.")
        print()
    #
    #END