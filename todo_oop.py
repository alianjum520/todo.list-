from datetime import datetime
from enum import Enum

class status(Enum):
    completed = 1
    doing = 2
    incomplete = 3
    

class Task(): 
    _data = []
    _task_dict = {}
    def __init__(self,id,task_name,creation_date):
        self.id = id
        self.task_name = task_name
        self.creation_date = creation_date
    def add(self):
        self._task_dict['id'] = self.id
        self._task_dict['task'] = self.task_name
        self._task_dict['creation_date'] = self.creation_date
        self._data.append(self._task_dict.copy())
        return self._data
    def update(self):
        search_id =  input("Enter the id of task you want to update: ")
        new_task = input("Enter thre new Task: ")
        for i in range(len(self._data)):
            if int(search_id) in self._data[i].values():
                self._data[i]['task'] = new_task
                self._data[i]['updated_date'] = self.creation_date 
            else:
                print("Value not found in the list")
        return self._data
    def delete(self):
        delete_id = input("which value do you need to delete: ")
        for i in range(len(self._data)):
            if int(delete_id) in self._data[i].values():
                self._data[i].clear()
            else:
                print("Value not found in the list")
        return self._data
    def mark_task(self):
        option = input('to mark task chose positive integer:\n1: Completed\n2: Doing\n3: Incomplete ')
        for i in range(len(self._data)):
            self._data[i]['status'] = status(int(option))
        
    def display(self):
        print(self._data)
        


choice = input("do you want to run program(yes/no): ")
i = 0

while(choice=='yes'):
    i = i + 1
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    new_task = input('Enter the new task:')
    obj = Task(i,new_task,time)
    obj.add()
    option = input('Do you want to update any task(yes/no): ')
    if option == 'yes': 
        obj.update()
    option2 = input('Do you want to delete any task(yes/no): ')
    if option2 == 'yes': 
        obj.delete()
    option3 = input('Do you want to mark any task(yes/no): ')
    if option3 == 'yes':
        obj.mark_task() 
    obj.display()
    choice = input("do you want to run program(yes/no): ")