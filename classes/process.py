class ownProcess:
    def __init__(self, pid, name, priority, status, exec_time):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.exec_time = exec_time
        self.status = status

    def add_proc():
        new_pid = int(input("Ввдедите PID процесса: "))
        new_name = input("Введите имя процесса: ")
        new_priority = int(input("Введите приоритет процесса: "))
        new_exec_time = int(input("Введите время выполнения: "))
        new_status = input("Введите статус: ")
        return ownProcess(new_pid, new_name, new_priority, new_exec_time, \
                          new_status)


    def __str__(self):
        return(f"PID: {self.pid}\nName: {self.name}\nPriority: {self.priority}\n\
Execution time: {self.exec_time}, State: {self.status}")