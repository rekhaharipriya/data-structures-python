# queue.py

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue element
    def enqueue(self, data):
        self.queue.append(data)

    # Dequeue element
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    # Peek element
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display queue
    def display(self):
        print("Queue elements:", self.queue)


# Example usage
if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    q.display()
    print("Front element:", q.peek())
    print("Dequeued element:", q.dequeue())
    q.display()
