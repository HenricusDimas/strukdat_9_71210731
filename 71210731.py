class Node:
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority
        self._next = None


class PriorityQueueUnsorted:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def add(self, data, priority):
        new_node = Node(data, priority)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node
        self._size += 1

    def remove(self):
        if self.is_empty():
            return

        if self._size == 1:
            current = self._head
            self._head = None
            self._tail = None
            del current
        else:
            min_priority = self._head._priority
            current = self._head
            prev = None
            min_prev = None

            while current is not None:
                if current._priority < min_priority:
                    min_priority = current._priority
                    min_prev = prev
                prev = current
                current = current._next

            if min_prev is None:
                self._head = self._head._next
            else:
                min_prev._next = min_prev._next._next

            if prev is self._tail:
                self._tail = min_prev

            del prev
        self._size -= 1

    def peek(self):
        if self.is_empty():
            return None
        else:
            min_priority = self._head._priority
            current = self._head
            while current is not None:
                if current._priority < min_priority:
                    min_priority = current._priority
                current = current._next

            current = self._head
            while current._priority != min_priority:
                current = current._next

            return current._data, current._priority

    def print_all(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            current = self._head
            print("== List Unsorted Queue ==")
            while current is not None:
                print(f"{current._priority} = {current._data}")
                current = current._next

    def ubahBersama(self, prio, namaBaru):
        current = self._head
        while current is not None:
            if current._priority == prio:
                current._data = namaBaru
            current = current._next

    def removePrioSekaligus(self):
        if self.is_empty():
            return

        highest_priority = self.peek()
        current = self._head
        while current is not None:
            if current._priority == highest_priority[1]:
                if current is self._head:
                    self._head = current._next
                else:
                    prev._next = current._next
                if current is self._tail:
                    self._tail = prev
                temp = current
                current = current._next
                del temp
                self._size -= 1
            else:
                prev = current
                current = current._next

myQueue = PriorityQueueUnsorted()
myQueue.add("Dedi",4)
myQueue.add("sindu",2)
myQueue.add("Hanif",5)
myQueue.add("Farel",2)
myQueue.add("Beatrix",3)
myQueue.add("Shalom",3)
myQueue.add("Hareis",2)
myQueue.print_all()

myQueue.ubahBersama(2,"mahasiswa A")
myQueue.print_all()

myQueue.removePrioSekaligus()
myQueue.print_all()
