from datetime import datetime
from enum import Enum
import json
class status(Enum):
    completed = 1
    doing = 2
    incomplete = 3

class Task(): 
    def __init__(self,id,task_name,creation_date,update_date,stat):
        self.__id = id
        self.__task_name = task_name
        self.__creation_date = creation_date
        self.__update_date = update_date
        self.___stat = stat
        
    def get_id(self):
        return self.__id
    def get_task_name(self):
        return self.__task_name
    def get_creation_date(self):
        return self.__creation_date
    def get_update_date(self):
        return self.__update_date
    def get_stat(self):
        return self.___stat
    def set_id(self,id):
        self.__id = id
    def set_task_name(self,task_name):
        self.__task_name = task_name
    def set_creation_date(self,creation_date):
        self.__creation_date = creation_date
    def set_update_date(self,update_date):
        self.__update_date = update_date
    def set_stat(self,stat):
        self.___stat = stat
    
def add(obj_list):
    num_task = int(input("Enter the number of task you want to Enter: "))
    for i in range(num_task):
        obj_list.append(Task("0","0","0",None,None))
    for obj in obj_list:
        id  = input("Enter the id: ")
        obj.set_id(id)
        task = input("Enter the task: ")
        obj.set_task_name(task)
        now = datetime.now()
        time = now.strftime("%d/%m/%Y %H:%M:%S")
        obj.set_creation_date(time)
        opt = int(input("Enter the status of the task\n1:Completed\n2:Doing\n3:incomplete\n"))
        x =status(opt)
        obj.set_stat(str(x))
    return obj_list 
def update(obj_list):
    upd_id = input("Enter the id you want to update: ")
    for obj in obj_list:
        if upd_id == obj.get_id():
            task = input("Enter the task: ")
            obj.set_task_name(task)
            now = datetime.now()
            time = now.strftime("%d/%m/%Y %H:%M:%S")
            obj.set_update_date(time)
            opt = int(input("Enter the status of the task\n1:Completed\n2:Doing\n3:incomplete\n"))
            x =status(opt)
            obj.set_stat(str(x))
        else:
            print("Value Not Found")
    return obj_list
def delete(obj_list):
    del_id = input("Enter the id you want to delete: ")
    for i,obj in enumerate(obj_list):
        if obj.get_id() == del_id:
            del obj_list[i]
            break
    return obj_list
def save_file(obj_list):
    file_name = input("Enter the name of the file:")
    text_file = open(f'{file_name}.json','w+')
    for i in range(len(obj_list)):
        text_file.write(json.dumps(obj_list[i].__dict__) + "\n")
    text_file.close()    
    
def show_menu():
    print("MENU")
    print("1: Add any task in list")
    print("2: Update any task from the list")
    print("3: Delete any task from list")
    print("4: Print your task list")    
    print("5: Save file in json format") 
    
    
    value = input("Enter your choice(please the choice should not be in negative value):")
    return value


def main():
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