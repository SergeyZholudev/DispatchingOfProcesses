# class for managing of the list of PID

import psutil
from process import ownProcess

def sorting_by_name(arr: list) -> list:
    """Функция сортировки списка имен процессов"""
    return arr.sort()
    
# формирование словаря key=pid, value='всё остальное'
processes_dict = {}
for proc in  psutil.process_iter(['pid', 'name', 'status']):
    process_obj = ownProcess(proc.info['pid'], proc.info['name'], proc.info['status'])
    processes_dict[process_obj.pid] = (proc.info['name'], proc.info['status'])

# получение списка имен процессов
processes_names = []
for procName in psutil.process_iter(['name']):
    processes_names.append(procName.info['name'])

# сортировка списка списка имен процессов
sorting_by_name(processes_names)
