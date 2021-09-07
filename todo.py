import sys
import os

#To add tasks in your list 
def add_items(list_data):
    add_value = input("Enter the value you want to add in the list :")
    list_data.append(add_value)
    return list_data

#TO update any certain task from your list 
def update_items(list_data):
    update_value = input("which value do you need to update: ")
    if update_value in list_data:
        index_value = list_data.index(update_value)
        new_value = input("Enter the new value: ")
        list_data[index_value] = new_value
    else:
        print("Value not found in the list")
    return list_data

#Tp delete a certain task from a list
def delete_items(list_data):
    delete_value = input("which value do you need to delete: ")
    if delete_value in list_data:
        list_data.remove(delete_value)
    else:
        print("Value not found in the list")
    return list_data

#To mark your tasks 
def mark_task(list_data):
    for i in range(len(list_data)):
        variable = input(f"Task: {list_data[i]}  completed yes/no: ")
        if variable == 'yes':
            print(f'{list_data[i]} \t ☑')
            list_data[i] = f'{list_data[i]} \t ☑'
            
        else:
            print(f'{list_data[i]} \t ☐')
            list_data[i] = f'{list_data[i]} \t ☐'
    return list_data
            
#Print method   
def print_list(list_data):
    print(list_data)

# Menu for your commands to run 
def show_menu():
    print("MENU")
    print("1: Add any task in list")
    print("2: Update any task from the list")
    print("3: Delete any task from list")
    print("4: Print your task list")    
    print("5: Mark tasks after adding the tasks in list ") 
    print("6: Mark your job complete and exit:")
    print("7: if your job is incomplete and you want to exit:")
    
    value = input("Enter your choice(please the choice should not be in negative value):")
    return value

# This Function is used for system termination
def system_close():
    print("ValueError: program crashed")
    sys.exit(0)

# This Function is used to mark job complete as in file     
def mark_job_completed(list_data,name_file):
    if os.path.exists(f'{name_file}.txt'):
        old_name = f'{name_file}_incomplete.txt'
        new_name = f'{name_file}_completed.txt'
        os.rename(old_name,new_name)
        text_file = open(f'{name_file}_completed.txt','w+')
        for element in list_data:
            text_file.write(element + "\n")
        text_file.close()
    else:
        text_file = open(f'{name_file}_completed.txt','w+')
        for element in list_data:
            text_file.write(element + "\n")
        text_file.close()

# This Function is used to mark job complete as in file
def mark_job_incomplete(list_data,name_file):
    if os.path.exists(f'{name_file}_incomplete.txt'):
        text_file = open(f'{name_file}_incomplete.txt','r+')
        for element in list_data:
            text_file.write(element + "\n")
        text_file.close()
    else:
        text_file = open(f'{name_file}_incomplete.txt','w+')
        for element in list_data:
            text_file.write(element + "\n")
        text_file.close()

# The main function for main interperter
def main():
    file_name = input("Enter the name of the file:")
    if os.path.exists(f'{file_name}_incomplete.txt'):
        data = []
        text_file = open(f'{file_name}_incomplete.txt','r+')
        x = text_file.readlines()
        for element in x:
            data.append(element.rstrip())
        print(data)
        text_file.close()
    else:
        data = []         
    choice =show_menu() 
    while(choice!='8'):
        if choice > '0' and choice <= '7': 
            if choice == '1':
                data = add_items(data)
            elif choice == '2':
                data = update_items(data)
            elif choice == '3':
                data = delete_items(data)
            elif choice == '4':
                print_list(data)
            elif choice == '5':
                data=mark_task(data)
            elif choice == '6':
                data = mark_job_completed(data,file_name)
                system_close()
            else:
                data=mark_job_incomplete(data,file_name)
                system_close()    
            choice =show_menu()         
        else:
            system_close()
    
    else:
            system_close()


#Python interperter running as main program 
if __name__ == '__main__':
    main()
