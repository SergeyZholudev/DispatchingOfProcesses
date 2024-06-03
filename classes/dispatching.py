# class for managing of the list of PID

import psutil
from process import ownProcess

# def sorting_by_name(arr: list) -> list:
#     """Функция сортировки списка имен процессов"""
#     return arr.sort()
    
# формирование словаря key=pid, value='всё остальное'
processes_dict = {}
for proc in  psutil.process_iter(['pid', 'name', 'status']):
    process_obj = ownProcess(proc.info['pid'], proc.info['name'], proc.info['status'])
    processes_dict[process_obj.pid] = (proc.info['name'], proc.info['status'])

# получение списка имен процессов
processes_names = []
for procName in psutil.process_iter(['name']):   # получаем список тек.процессов
    processes_names.append(procName.info['name']) # формируем список

sorted_list = sorted(processes_names)
for i in sorted_list:
    print(i)
