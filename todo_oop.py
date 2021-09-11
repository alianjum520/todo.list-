"""
    Returns:
        This module part: To import different
        python libraries
"""
from datetime import datetime
from enum import Enum
import json
class STATUS(Enum):
    """[summary]
    Args:
        Enum (Status): This is to check the status
        of the task different type of status
    """
    COMPLETED = 1
    DOING = 2
    INCOMPLETE = 3

class Task():
    """
    this is class which works as a datatype and
    store different values
    """
    def __init__(self,id_,task_name,creation_date,update_date,stat):
        self.__id = id_
        self.__task_name = task_name
        self.__creation_date = creation_date
        self.__update_date = update_date
        self.___stat = stat

    def get_id(self):
        """ This is getter method for an id """
        return self.__id
    def get_task_name(self):
        """ This is getter method for task Name """
        return self.__task_name
    def get_creation_date(self):
        """ This is getter method for the Creation date """
        return self.__creation_date
    def get_update_date(self):
        """ This is getter method for the update date """
        return self.__update_date
    def get_stat(self):
        """ This is getter method for the status"""
        return self.___stat
    def set_id(self,id_):
        """ This is setter method for an id"""
        self.__id = id_
    def set_task_name(self,task_name):
        """ This is setter method for the task name """
        self.__task_name = task_name
    def set_creation_date(self,creation_date):
        """ This is setter method for the creation date """
        self.__creation_date = creation_date
    def set_update_date(self,update_date):
        """ This is setter method for update date """
        self.__update_date = update_date
    def set_stat(self,stat):
        """ This is setter method for the status """
        self.___stat = stat

def add(obj_list):
    """

    Args:
        obj_list (list): Takes a list as an argument to add data init after
                         that return the list

    Returns:
        [list]: Returns the object list after appending items in it
    """
    num_task = int(input("Enter the number of task you want to Enter: "))
    for i in range(num_task):
        obj_list.append(Task("0","0","0",None,None))
    for obj in obj_list:
        id_  = input("Enter the id: ")
        obj.set_id(id_)
        task = input("Enter the task: ")
        obj.set_task_name(task)
        now = datetime.now()
        time = now.strftime("%d/%m/%Y %H:%M:%S")
        obj.set_creation_date(time)
        opt = int(input("Enter the status of the task\n1:Completed\n2:Doing\n3:incomplete\n"))
        x =STATUS(opt)
        obj.set_stat(str(x))
    return obj_list
def update(obj_list):
    """
    This is the update function this updates the values or task
    using the id of the obj stored in a list but id is not updated
    after that it add update time in the list of object which object
    is updated it will only update the function that exists and is
    being searched

    Args:
        obj_list (list): takes the object list and looks how many objects are there

    Returns:
        obj_list [list]: return the updated list
    """

    upd_id = input("Enter the id you want to update: ")
    for obj in obj_list:
        if upd_id == obj.get_id():
            task = input("Enter the task: ")
            obj.set_task_name(task)
            now = datetime.now()
            time = now.strftime("%d/%m/%Y %H:%M:%S")
            obj.set_update_date(time)
            opt = int(input("Enter the status of the task\n1:Completed\n2:Doing\n3:incomplete\n"))
            x =STATUS(opt)
            obj.set_stat(str(x))
        else:
            print("Value Not Found")
    return obj_list
def delete(obj_list):
    """
    This function searches the  id you want to delete from list
    if it  finds that it will delete that

    Args:
        obj_list (list): [brings all the list of objects that have been created]

    Returns:
        obj_list (list): [updated list after deleting the object we want ]
    """
    del_id = input("Enter the id you want to delete: ")
    for i,obj in enumerate(obj_list):
        if obj.get_id() == del_id:
            del obj_list[i]
            break
    return obj_list
def save_file(obj_list):
    """
    This function just saves the file in json format

    Args:
        obj_list (list): saves all the data  present in list as in json format
    """
    file_name = input("Enter the name of the file:")
    text_file = open(f'{file_name}.json','w+')
    for i in range(len(obj_list)):
        text_file.write(json.dumps(obj_list[i].__dict__) + "\n")
    text_file.close()

def show_menu():
    """
    This is the menu function as the program is
    menu driven program so it shows the options
    and choices in this program

    Returns:
        value[str]: [this function returns value of choices as a string]
    """
    print("MENU")
    print("1: Add any task in list")
    print("2: Update any task from the list")
    print("3: Delete any task from list")
    print("4: Print your task list")
    print("5: Save file in json format")


    value = input("Enter your choice(please the choice should not be in negative value):")
    return value


def main():
    """
    this is the main function in which the whole program executes
    it just acts like a c++ main function or we can say its an interpreter
    it is called through the dunder method
    """
    obj_list = []
    choice =show_menu()
    while(choice!='8'):
        if choice > '0' and choice <= '7':
            if choice == '1':
                obj_list = add(obj_list)
            elif choice == '2':
                obj_list = update(obj_list)
            elif choice == '3':
                obj_list = delete(obj_list)
            elif choice == '4':
                for i in range(len(obj_list)):
                    string = json.dumps(obj_list[i].__dict__)
                    print(string)
            elif choice == '5':
                save_file(obj_list)
            choice =show_menu()

#Python interperter running as main program
if __name__ == '__main__':
    main()
