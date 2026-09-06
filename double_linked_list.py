class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def remove(self, value):
        current = self.head

        while current is not None:

            if current.value == value:

                if current.previous is not None:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous

                return True

            current = current.next

        return False

    def forward(self):
        values = []
        current = self.head

        while current is not None:
            values.append(current.value)
            current = current.next

        return values

    def backward(self):
        values = []
        current = self.tail

        while current is not None:
            values.append(current.value)
            current = current.previous

        return values


if __name__ == "__main__":

    history = DoublyLinkedList()

    history.append("Home")
    history.append("Search")
    history.append("Product")
    history.append("Checkout")

    print("Forward:")
    print(history.forward())

    print("\nBackward:")
    print(history.backward())

    history.remove("Product")

    print("\nAfter removing Product:")
    print(history.forward())