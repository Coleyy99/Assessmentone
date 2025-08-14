#Sets/saves text file
Expense_file = "expense_file.txt"

#begins loop.
while True :
#Display menu to user of options.
    print("\nExpense tracker:")
    print("1. View Expenses tracked")
    print("2. Enter new Expenses")
    print("3. Clear Expense list")
    print("4. Exit")
#requests user input 
    choice = input("Enter your choice: ")

#Begins if/elif/else loop for options.
#Option one, prints text file line by line.
    if choice == "1":
        with open(Expense_file, "r") as file: 
            for line in file: 
                print(line, end="") 
#Option two, requested user input for expense and amounts, system then 
# formulates a sentance to save to the text file. 
    elif choice == "2":
        Expense_name = input("Enter type of Expense: ")
        Expense_amount = input("Enter the amount you spent: ")
        with open(Expense_file, "a") as file:
            Entry = Expense_name + " " + "$" + Expense_amount + "\n"
            file.write(Entry) 
#Option three, clears the text file for a fresh start. 
    elif choice == "3": 
        with open(Expense_file , "w") as file:
            file.write("")
        print("Tracker has been cleared")
#Option four, prints good bye message to user. 
# added break to loop here.
    elif choice == "4":
        print("Thank you and good-bye")
        break
#Last, unknown option, is for if a user input is not 1-4. 
    else:
        print("Invalid choice, please try again.")
        







        