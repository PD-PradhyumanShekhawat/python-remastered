class Deque:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def add_front(self, value):
        self.data.insert(0, value)

    def add_rear(self, value):
        self.data.append(value)

    def remove_front(self):
        if self.is_empty():
            return None

        return self.data.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return None

        return self.data.pop()

    def peek_front(self):
        if self.is_empty():
            return None

        return self.data[0]

    def peek_rear(self):
        if self.is_empty():
            return None

        return self.data[-1]

    def display(self):
        print(self.data)


if __name__ == "__main__":
    deque = Deque()

    deque.add_rear(10)
    deque.add_rear(20)
    deque.add_front(5)

    deque.display()

    print("Front:", deque.peek_front())
    print("Rear:", deque.peek_rear())

    print("Removed from front:", deque.remove_front())
    print("Removed from rear:", deque.remove_rear())

    deque.display()