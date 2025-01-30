#Function to add a new task to the list
def add_task(list_task):
    task = input("Enter task : ")
    list_task.append(task)
    print("\nNew task added successfully!!")
    show_list(list_task)

#Function to display the list
def show_list(list_task):
    if  list_task:

        print("==========The current TO-DO List is==========")

        for index,c in enumerate(list_task): #alwasys write index before the main content
            print(f"{index+1}. {c}")


    else:
        #The case if the list is empty
        print("OOPS!! The list is empty")

#Function to remove a task from the list 
def remove_task(list_task):
    try:
        #We take the index of the task to be deleted as input
        index = int(input("Enter the index number of the task that you want to delete : "))
        if index <= 0 or index > len(list_task):
            print("Invalid Input!!!Please Check")
            return 

        list_task.pop(index-1)
        print(f"Task deleted successfully!!")
        show_list(list_task)
    except ValueError:
        print("Invalid Input!!!! Please enter an integer")

#The main menu that consists of different choices
def main_menu():
        print("======================Welcome to To-Do List======================")
        print("1. Display Tasks  ")
        print("2. Add a new Task")
        print("3. Remove a Task")
        print("4. Exit the List")
        

def main():
    list_task = []
    while(True):
        main_menu()
        try:
            #Taking the choice of the user as input
            choice = int(input("Make your choice : "))

            if choice<=0 or choice>4:
                print("Invalid Input!!")
                print(" Try again")
                continue

            if choice == 1 :
                show_list(list_task)
            elif choice == 2:
                add_task(list_task)
            elif choice == 3:
                remove_task(list_task)
            elif choice == 4 :
                print("Exit List!!!! Thank you for using")
                break
        except ValueError:
            #If the user has input some other thing rather than an integer within the range
            print("\nInvalid Input!!! Please enter a number between 1 to 4")



main()