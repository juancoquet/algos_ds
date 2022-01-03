from linked_list import Node


class OrderedList:
    
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if not previous:
            self.head = current.next
        else:
            previous.next = current.next
        return current.data
    
    def index(self, item):
        current = self.head
        idx = 0
        while current:
            if current.data == item:
                return idx
            else:
                current = current.next
                idx += 1

    def pop(self):
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next
        if previous:
            previous.next = None
        else:
            self.head = None
        return current.data

    def search(self, item):
        current = self.head
        found = False
        exceeded = False
        while current and not found and not exceeded:
            if current.data == item:
                found = True
            else:
                if current.data > item:
                    stop = True
                else:
                    current = current.next
        return found

    def add(self, item):
        current = self.head
        previous = None
        position_found = False
        while current and not position_found:
            if current.data > item:
                position_found = True
            else:
                previous = current
                current = current.next
        
        new_node = Node(item)
        if not previous:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = current
            previous.next = new_node
