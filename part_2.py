#Creates the list in Python
book_list = ["Fourth Wing","Iron Flame"]

#defines the function of viewing books
#Begins if/else statement
#If something is on the list, it prints the list, one title at a time
#If nothing on list, print message to user
def view_books():
    if book_list:
        print ("\nYour library: ")
        for book in book_list:
            print(book, sep='\n', end='\n')
    else: 
        print('\nNo books added to your library yet.')

#Defines the function of clearing the list
#clears list and informs user 
def clear_library():
    book_list.clear()
    print("All books have been cleared")

#Begins while loop
#Dispays opening message to users letting them know their options 
while True: 
    print("\n Library Menu:")
    print("1. View your books in a list.")
    print('2. Add a book to your library.')
    print("3. Clear your library.")
    print("4. Exit.")

#Requests input from user to make selection (1-5) 
    choice = input("choose an option (1-4): ")

#Begins if/elif/else statement
#Uses User input to cycle through options
#1st option begins the fuction definded before, view_books
    if choice == '1':
        view_books()
#2nd option is to add a book, unable to work out how to define this
#sets user input to title, requests title from user 
#Adds title to end of list
    elif choice == '2':
        title = input("Enter the title of the book to add: ")
        book_list.append(title)
#3rd option is to clear library using definded function clear_library
    elif choice == '3':
        clear_library()
#4th option is to exit loop
#prints exitmessage to user 
    elif choice == '4':
        print("Thank you and goodbye.")
        break
#safety net inplace, incase user enters any other then what i intended. 
    else:
        print("Invaild entry, please make a selection between 1 and 5")








        