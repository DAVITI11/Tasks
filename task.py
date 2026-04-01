import datetime
import time

def logger(action_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            print(f"Action: {action_type} | Function: {func.__name__} | Start: {datetime.datetime.now()}")
            rs = func(*args, **kwargs)
            end = time.time()
            print(f"Finished: {func.__name__} | Time: {end - start} \n")
            return rs
        return wrapper
    return decorator


class Task:
    def __init__(self, id, dasaxeleba, prioriteti, vada):
        self.id = id
        self.dasaxeleba = dasaxeleba
        self.statusi = 'momlodine'
        self.prioriteti = prioriteti
        self.vada = vada
    @property
    def prioriteti(self):
        return self.__prioriteti
    @prioriteti.setter
    def prioriteti(self, value):
        if 0 < value < 6:
            self.__prioriteti = value
        else:
            print("პრიორიტეტი უნდა იყოს 1-5")
    def CmpStatusi(self,vl):
        self.statusi = vl
    def printInfo(self):
        print(f"ID = {self.id} დასახელება = {self.dasaxeleba} სტატუსი = {self.statusi} პრიორიტეტი = {self.prioriteti} ვადა = {self.vada} \n")


class TaskManager:

    def __init__(self):
        self.tasks = []

    @logger("ტასკის დამატება")
    def damatebataskis(self, tsk):
        for i in self.tasks:
            if i.id == tsk.id:
                print("ასეთი ID უკვე არსებობს")
                return
        self.tasks.append(tsk)

    @logger("დასრულებული ტასკი")
    def taskisdasrulda(self, id):
        for t in self.tasks:
            if t.id == id:
                t.CmpStatusi('gashvebuli')
                print("ტასკი დასრულდა")
                t.CmpStatusi('dasrulebuli')
                return
        print("ტასკი ვერ მოიძებნა")

    @logger("ტასკის წაშლა")
    def washla(self, index):
        if 0 <= index < len(self.tasks):
            print(f"ტასკი წაიშალა (index {index})")
            self.tasks.pop(index)
        else:
            print("არასწორი ინდექსი")

    def dasrulebuliTaskebi(self):
        for t in self.tasks:
            if t.statusi == 'dasrulebuli':
                yield t

    def showAll(self):
        for t in self.tasks:
            t.printInfo()

t = Task(1, "რწწწწ", 3, "2026-04-10")
ts = TaskManager()
ts.damatebataskis(t)
ts.taskisdasrulda(1)
ts.showAll()