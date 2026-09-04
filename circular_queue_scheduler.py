class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity

        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, task):
        if self.is_full():
            print("Queue is full. Cannot schedule:", task)
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = task
        self.size += 1

        return True

    def dequeue(self):
        if self.is_empty():
            return None

        task = self.data[self.front]

        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return task

    def peek(self):
        if self.is_empty():
            return None

        return self.data[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        tasks = []

        for i in range(self.size):
            index = (self.front + i) % self.capacity
            tasks.append(self.data[index])

        print("Scheduled tasks:", tasks)


if __name__ == "__main__":

    scheduler = CircularQueue(5)

    scheduler.enqueue("Process log files")
    scheduler.enqueue("Run unit tests")
    scheduler.enqueue("Build application")
    scheduler.enqueue("Deploy application")

    scheduler.display()

    print("Executing:", scheduler.dequeue())
    print("Executing:", scheduler.dequeue())

    scheduler.enqueue("Generate report")
    scheduler.enqueue("Backup database")

    scheduler.display()

    print("Next task:", scheduler.peek())