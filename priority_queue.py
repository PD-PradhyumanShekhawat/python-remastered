class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, task):
        self.heap.append(task)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._bubble_down(0)

        return minimum

    def _bubble_up(self, index):
        while index > 0:
            parent = self.parent(index)

            if self.heap[index][0] >= self.heap[parent][0]:
                break

            self.heap[index], self.heap[parent] = (
                self.heap[parent],
                self.heap[index]
            )

            index = parent

    def _bubble_down(self, index):
        while True:
            left = self.left_child(index)
            right = self.right_child(index)

            smallest = index

            if (
                left < len(self.heap)
                and self.heap[left][0] < self.heap[smallest][0]
            ):
                smallest = left

            if (
                right < len(self.heap)
                and self.heap[right][0] < self.heap[smallest][0]
            ):
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index]
            )

            index = smallest

    def is_empty(self):
        return len(self.heap) == 0


if __name__ == "__main__":

    scheduler = MinHeap()

    tasks = [
        (3, "Generate report"),
        (1, "Handle production incident"),
        (4, "Clean temporary files"),
        (2, "Run database backup"),
        (1, "Restart failed service")
    ]

    for task in tasks:
        scheduler.insert(task)

    print("Execution order:")

    while not scheduler.is_empty():
        priority, task = scheduler.extract_min()
        print(f"Priority {priority}: {task}")