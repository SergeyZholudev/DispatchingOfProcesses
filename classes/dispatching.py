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
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            process_obj = ownProcess(proc.info['pid'], \
                                    proc.info['name'], \
                                    priority_gen(), \
                                    proc.info['status'], \
                                    exec_time_gen()
            )
            processes[process_obj.pid] = [process_obj.name, \
                                            process_obj.priority, \
                                            process_obj.status, \
                                            process_obj.exec_time]
        
        return processes

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
        # получаем список приоритетов
        priorities = []
        description = []
        priority_dict = self.get_all()
        for key, value in priority_dict.items():
            priorities.append(value[1])

        def qSort(arr) -> list:
            """Быстрая сортировка массива"""
            if len(arr) <= 1:
                return arr
            else:
                mid = arr[len(arr)//2]
                s_nums = []
                m_nums = []
                e_nums = []
                for n in arr:
                    if n < mid:
                        s_nums.append(n)
                    elif n > mid:
                        m_nums.append(n)
                    else:
                        e_nums.append(n)
                return qSort(s_nums) + e_nums + qSort(m_nums)

        return qSort(priorities)
        