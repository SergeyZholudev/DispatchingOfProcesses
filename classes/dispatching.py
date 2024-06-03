# class for managing of the list of PID

import psutil
from classes.process import ownProcess

class Dispatching:
    def __init__(self):
        pass
    
    def get_all(self):
        """Получение словаря key=pid, value=всё остальное"""
        processes_dict = {}
        for proc in  psutil.process_iter(['pid', 'name', 'status']):
            process_obj = ownProcess(proc.info['pid'], proc.info['name'], proc.info['status'])
            processes_dict[process_obj.pid] = (proc.info['name'], proc.info['status'])
        for key,value in processes_dict.items():
            print(key)
            print(value)

    def get_names(self) -> list:
        """Несортированный список имен процессов"""
        processes_names = []
        for procName in psutil.process_iter(['name']):   # получаем список тек.процессов
            processes_names.append(procName.info['name']) # формируем список
        return processes_names
    
    def get_sorted_by_name(self) -> list:
        """Сортированный список имен процессов"""
        processes_names = self.get_names()
        sorted_list = sorted(processes_names)
        return sorted_list
