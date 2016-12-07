class BinaryHeap(object):

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percent_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i //= 2

    def percent_down(self, i):
        while (i * 2) <= self.current_size:
            min_child = self.min_child(i)

            if self.heap_list[i] > self.heap_list[min_child]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child]
                self.heap_list[min_child] = temp
            i = min_child

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.percent_up(self.current_size)

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete_min(self):
        return_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percent_down(1)
        return return_value

    def is_empty(self):
        pass

    def size(self):
        pass

    def build_heap(self, list):
        i = len(list) // 2
        self.current_size = len(list)
        self.heap_list = [0] + list[:]
        while i > 0:
            self.percent_down(i)
            i -= 1

pq = BinaryHeap()
pq.build_heap([1, 2, 3, 1000])
pq.build_heap([101, 200, 2, 4, 100])
print pq.heap_list
