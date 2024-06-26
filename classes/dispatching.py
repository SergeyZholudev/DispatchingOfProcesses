# класс для работы с реальными процессами ОС

import random
import psutil
from classes.process import ownProcess

class Dispatching:
    def __init__(self):
        pass

    def qSort(self, arr) -> list:
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
            return self.qSort(s_nums) + e_nums + self.qSort(m_nums)
    
    def binary_search(self, arr: list, pid) -> bool:
        """Функция двоичного поиска"""
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if pid == arr[mid]:
                return True
            if pid > arr[mid]:
                low = mid + 1
            elif pid < arr[mid]:
                high = mid - 1
  
    def get_all(self):
        """Получение словаря key=pid, value=всё остальное"""

        def priority_gen() -> dict:
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
    
    def get_sorted_priority(self) -> list:
        """Сортировка по приоритету"""
        priorities = []
        priority_dict = self.get_all()
        for key, value in priority_dict.items():
            priorities.append(value[1])

        return self.qSort(priorities)
    
    def get_sorted_execTime(self) -> list:
        """Сортировка по времени исполнения"""
        exec_time = []
        time_dict = self.get_all()
        for key, value in time_dict.items():
            exec_time.append(value[3])

        return self.qSort(exec_time)
    
    def searching_by_pid(self):
        """Поиск процесса по PID"""
        processes_pid = []
        for proc in psutil.process_iter(['pid']):   # формируем список pid
            processes_pid.append(proc.info['pid'])
        # print(processes_pid)
        while True:
            try:
                user_pid = int(input("Введите PID процесса: "))
                break
            except:
                print("Введённая величина должна быть числом.")
        if self.binary_search(processes_pid, user_pid):
            processes_dict = self.get_all()
            print("*" *40)
            print(processes_dict[user_pid])
            print("*" *40)
        else:
            print("Процесса с таким PID нет.")

    def searching_by_name(self) -> None:
        """Поиск информации о процессе по имени."""
        processes_names = self.get_all()
        user_proc_name = input("Введите имя процесса: ")
        for key, value in processes_names.items():
            if value[0].lower() == user_proc_name.lower():
                print("*" *40)
                print(f"PID: {key}")
                print(f"INFO: {value}")
                print("*" *40)
                