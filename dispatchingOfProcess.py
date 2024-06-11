# the main code for dispacthing of process in OS:
# This project is about managing of process in OS. We store the list of proccess with the next attributes:
# id of process
# name of process
# time of execution
# priotiry of process
# state of process By this script we can:
# search of process by PID
# search of process by name Process dispatching have to use stack and queue mechanisms. 
#  FIFO for low priority process. LIFO for low priority process.
# we can change state o processes
# add process
# delete process
# This project has test purpose and is needed for understanding of stack and 
# queue mechanisms, basic principles of OOP and practice of soling real issues.

import os
import queue

from classes.dispatching import Dispatching
from classes.process import ownProcess

# создаём две приоритетные очереди 
q_high = queue.Queue()
q_low = queue.Queue()

def queuing():
    """Добавляем процесс в очереди, на основании значения
    приоритета либо в high priority, либо в low priority очередь."""
    for i in range(5):
        temp_proc = ownProcess.add_proc()
        if temp_proc.priority <= 15:
            q_high.put(temp_proc)
        else:
            q_low.put(temp_proc)

def queue_show():
    """Показываем состав очередей."""
    if not q_high.empty():
        print(f"\nОчередь высокого приоритета: \n{q_high.get()}\n")
    else:
        print(f"\nОчередь высокого приоритета пуста.")
    if not q_low.empty():
        print(f"\nОчередь низкого приоритета: \n{q_low.get()}\n")
    else:
        print(f"\nОчередь низкого приоритета пуста. \n")

# основной код программы, взаимодействие с пользователем и т.д.
print("Данное ПО предназначено для получения список процессов в данный момент.")

while True:
    print("""1. Получение списка процессов(pid, name, priority, status)
2. Получение списка имен процессов запущенных на ПК.
3. Сортировка списка имен процессов по алфавиту.
4. Сортировка процессов по приоритету.
5. Сортировка процессов по времени исполнения.
6. Поиск процесса по PID.
7. Поиск процесса по имени.
8. Добавить процесс.
9. Показать процесс из очереди с высоким приоритетом(LIFO - стэк).
10. Показать процесс из очереди с низкиим приоритетом(FIFO). 
99. Очистить экран.
00. Выход из программы.
""")
    
    action = int(input("Введите номер требуемой операции: "))
    dispatching_obj = Dispatching()

    match action:
        case 1:
            for key, value in dispatching_obj.get_all().items():
                print(key)
                print(value)
        case 2:
            for proc in dispatching_obj.get_names():
                print(proc)
        case 3:
            for proc in dispatching_obj.get_sorted_by_name():
                print(proc)
        case 4:
            for i in dispatching_obj.get_sorted_priority():
                print(f"Priority: {i}")
        case 5:
            for i in dispatching_obj.get_sorted_execTime():
                print(f"Exec time: {i}")
        case 6:
            dispatching_obj.searching_by_pid()
        case 7:
            dispatching_obj.searching_by_name()
        case 8:
            queuing()
        case 9:
            queue_show()
        case 99:
            os.system('cls')
        case 00:
            break
        case _:
            print("Надо что-то выбрать из меню.")
