# stack.py

class Stack:
    def __init__(self):
        self.stack = []

    # Push element
    def push(self, data):
        self.stack.append(data)

    # Pop element
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    # Peek element
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        print("Stack elements:", self.stack)


# Example usage
if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)

    s.display()
    print("Top element:", s.peek())
    print("Popped element:", s.pop())
    s.display()
