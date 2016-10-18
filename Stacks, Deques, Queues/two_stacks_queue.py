class TwoStacksQueue():

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, element):
        self.in_stack.append(element)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

queue = TwoStacksQueue()
# self.in_stack = [0, 1, 2, 3, 4]
queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)


# Append from in_stacks pops in reverse e.g. out_stack = [4] ... out_stack = [4, 3, 2] ... out_stack = [4, 3, 2, 1, 0]
# Once the lists have been copied over. Pop the element e.g.
# [4, 3, 2, 1]
# [4, 3, 2]
# [4, 3]
# [4]
queue.dequeue()

print queue.out_stack # Pop [0], which was entered in first. These 2 stacks are behaving like a queue now.
