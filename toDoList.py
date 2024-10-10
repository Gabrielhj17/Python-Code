tasks = []

def menu():
    print("")
    print("What would you like to do?")
    print("1. Add a task to the list")
    print("2. Remove a task from the list")
    print("3. View all tasks")
    print("4. Exit")
    selection = int(input("Choose an option of 1 through 4: "))
    print("")
    switchboard(selection)
    return selection

def switchboard(selection):
    if selection == 1:
        addItem()
    elif selection == 2:
        deleteItem()
    elif selection == 3:
        viewItems()
    elif selection == 4:
        print("Goodbye!")
    else:
        print("Invalid input. Please try again.")
        menu()

def addItem():
    itemToAdd = str(input("What would you like to add to the list? "))
    tasks.append(itemToAdd)
    repeat = str(input("Task added successfully. Would you like to add another task? (y/n) "))
    if repeat == "y" or repeat == "Y" or repeat == "yes" or repeat == "yes":
        addItem()
    else:
        menu()

def deleteItem():
    if len(tasks) == 0:
        print("There are no tasks on the list, please add some before deleting")
        menu()
    taskItem = 1
    for task in tasks:
        print(f"{taskItem}. {task}")  
        taskItem += 1

    itemToDelete = int(input("What would you like to remove from the list? ")) - 1  
    if 0 <= itemToDelete < len(tasks):  
        tasks.pop(itemToDelete)
        if len(tasks) == 0:
            print("There are no tasks on the list")
            menu()
        else:
            print("Task removed successfully, new list of tasks as follows:")
    else:
        print("Invalid input. Please try again.")
        deleteItem()

    taskItem = 1
    for task in tasks:
        print(f"{taskItem}. {task}")  
        taskItem += 1

    repeat = str(input("Would you like to delete another task? (y/n) "))
    if repeat == "y" or repeat == "Y" or repeat == "yes" or repeat == "yes":
        deleteItem()
    else:
        menu()

def viewItems():
    if len(tasks) == 0:
        print("There are no tasks on the list, please add some before viewing")
        menu()
    taskItem = 1
    for task in tasks:
        print(f"{taskItem}. {task}")  
        taskItem += 1
    
    menu()

menu()