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
from classes.dispatching import Dispatching

print("Данное ПО предназначено для получения список процессов в данный момент.")

while True:
    print("""1. Получение списка процессов(pid, name, priority, status)
2. Получение списка имен процессов запущенных на ПК.
3. Сортировка списка имен процессов по алфавиту.
4. Сортировка процессов по приоритету.
5. Сортировка процессов по времени исполнения.
6. Поиск процесса по PID.
7. Поиск процесса по имени.
9. Очистить экран.
0. Выход из программы.
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
        case 9:
            os.system('cls')
        case 0:
            break
        case _:
            print("Надо что-то выбрать из меню.")
