class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def is_balanced(expression):
    stack = Stack()

    matching_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    opening_brackets = set(matching_brackets.values())

    for character in expression:

        if character in opening_brackets:
            stack.push(character)

        elif character in matching_brackets:
            if stack.is_empty():
                return False

            opening = stack.pop()

            if opening != matching_brackets[character]:
                return False

    return stack.is_empty()


if __name__ == "__main__":

    expressions = [
        "(a + b) * [c - d]",
        "{[()]}",
        "(a + b]",
        "((a + b)"
    ]

    for expression in expressions:
        result = is_balanced(expression)

        print(f"{expression} -> {result}")