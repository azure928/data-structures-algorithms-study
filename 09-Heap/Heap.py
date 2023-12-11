class MaxBinaryHeap: 
    def __init__(self): 
        self.items = []
        
    def insert(self, value):
        self.items.append(value)
        self.move_up()
        return self
    
    def move_up(self):
        child_idx = len(self.items) - 1
        while child_idx > 0:
            parent_idx = (child_idx - 1) // 2
            if self.items[child_idx] <= self.items[parent_idx]:
                break
            self.swap(child_idx, parent_idx)
            child_idx = parent_idx
    
    def swap(self, idx_1, idx_2):
        self.items[idx_1], self.items[idx_2] = self.items[idx_2], self.items[idx_1]
        
    def remove_max(self): 
        if not self.items:
            raise Exception("Heap is empty") 
        max_elem = self.items [0]
        end_idx= len(self.items) - 1
        self.swap(0, end_idx)
        self.items.pop()
        self.move_down()
        return max_elem
    
    def move_down(self):
        parent_idx = 0
        child_idx = 2 * parent_idx + 1 
        end_idx = len(self.items) - 1
        while child_idx <= end_idx:
            if child_idx < end_idx and self.items [child_idx] < self.items [child_idx + 1]:
                child_idx += 1
            if self.items [parent_idx] < self.items [child_idx]:
                self.swap(parent_idx, child_idx)
                parent_idx = child_idx
                child_idx = 2 * parent_idx + 1
            else:
                break
    

myheap = MaxBinaryHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.items)

myheap.remove_max()
print(myheap.items)

myheap.remove_max()
print(myheap.items)

