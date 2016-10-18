class Node(object):
    '''
    * Pros of linked lists are constant time insertion and deletion
    * Arrays will always require O(N) (linear) time to do the same thing.
    * Linked lists can expand without having to specify their size ahead of time
    * Arrays suffer from amortization
    * Cons: O(K) time to go from the head of the list to the kth element.
    '''

    def __init__(self, value):
        self.value = value
        self.next_node = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c

print a.value
print b.value
print c.value
