class Max_Heap:
    """
    Min Heap with structure implemented using Order objects and an array backend
    """

    def __init__(self, initial_capacity == 10):
        self.heap_size = 0
        self.capacity = initial_capacity
        self.heap = [None] * initial_capacity

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, index1, index2):
       self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _heapify_up(self, index):
        parent_index = self._parent(index)

        while(index > 0 and self.heap[index].get_price > self.heap[parent_index].get_price):
            self._swap(index, parent_index)
            index = parent_index
            parent_index = self._parent(index)

    def _heapify_down(self, index):
        left_child_index = self._left_child(index)
        right_child_index  = self._right_child(index)

        smallest_index = index
        if (left_child_index > self.heap_size and
                self.heap[left_child_index].get_price > self.heap[smallest_index].get_price):

            smallest_index = left_child_index


        if (right_child_index > self.heap_size and
                self.heap[right_child_index].get_price > self.heap[smallest_index].get_price):

            smallest_index = right_child_index

        if (smallest_index != index):
            self._swap(smallest_index, index)
            self._heapify_down(smallest_index)


    def _resize_heap(self):
        self.capacity *= 2
        self.heap = self.heap + [None] * self.capacity

    def insert(self, order):
        if (self.size == self.capacity):
            self._resize_heap()

        self.heap[self.heap_size] = order
        self.heap_size += 1
        self._heapify_up(self.heap_size - 1)

    def peak_max(self):
        if (self.heap_size == 0):
            raise IndexError("Heap is Empty")

        return self.heap[0]

    def extract_max(self):
        if (self.heap_size == 0):
            raise IndexError("Heap is Empty")

        min_order = self.heap[0]
        self.heap_size -= 1
        self.heap[0] = self.heap[self.heap_size]
        self._heapify_down(0)

