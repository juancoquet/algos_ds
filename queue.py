import random

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Printer:

    def __init__(self, ppm):
        self.ppm = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task:
            self.time_remaining -= 1
            if not self.time_remaining:
                self.current_task = None

    def busy(self):
        return self.current_task != None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.pages * 60/self.ppm

    


class Task:

    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.pages = random.randrange(1, 21)

    def wait_time(self, current_time):
        return current_time - self.timestamp



def new_print_task():
    return random.randrange(1, 181) == 180

def sim_print(seconds, ppm):
    printer = Printer(ppm)
    print_queue = Queue()
    wait_times = []

    for current_sec in range(seconds):
        if new_print_task():
            task = Task(timestamp=current_sec)
            print_queue.enqueue(task)

        if not printer.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            wait_times.append(next_task.wait_time(current_sec))
            printer.start_next(next_task)

        printer.tick()
    
    avg_wait_time = sum(wait_times) / len(wait_times)
    print(avg_wait_time, print_queue.size())


for _ in range(10):
    sim_print(3600, 5)