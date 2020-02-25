from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return len(self.storage)
