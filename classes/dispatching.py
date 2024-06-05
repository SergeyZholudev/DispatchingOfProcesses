# class for managing of the list of PID

import random
import psutil
from classes.process import ownProcess

class Dispatching:
    def __init__(self):
        pass
    
    def get_all(self):
        """Получение словаря key=pid, value=всё остальное"""

        def priority_gen() -> int:
            """генерация приоритета"""
            return random.randint(0, 31)
        
        def exec_time_gen():
            """генерация времени выполнения"""
            return random.randint(1, 1000)

        # формируем объекты, наполняем словарь процессов, так как priority
        # и execution time получить не можем, то генерим их самостоятельно
        processes = {}
        for proc in  psutil.process_iter(['pid', 'name', 'status']):
            process_obj = ownProcess(proc.info['pid'], \
                                    proc.info['name'], \
                                    priority_gen(), \
                                    proc.info['status'], \
                                    exec_time_gen()
            )
            processes[process_obj.pid] = (process_obj.name, \
                                            process_obj.priority, \
                                            process_obj.status, \
                                            process_obj.exec_time)
        # выводим на экран словарь
        for key,value in processes.items():
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
    
    def get_sorted_priority(self):
        priorities = []
        
