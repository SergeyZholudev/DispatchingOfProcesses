class ownProcess:
    def __init__(self, pid, name, priority, status, exec_time):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.exec_time = exec_time
        self.status = status

    def __str__(self):
        return(f"PID: {self.pid}\nName: {self.name}\nPriority: {self.priority}\n\
               Execution time: {self.exec_time}, State: {self.state}")