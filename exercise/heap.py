class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self ,value):
        # step 1 : put the value in the end of the heap

        self.heap.append(value)

        # step 2 : let it bubble up  to the right spot

        self.bubbleUp(len(self.heap) -1)

    def bubbleUp(self, index):

        while (index > 0):
            # find the parent index using a formula

            parentIndex = (index - 1 ) //2

            # if i am smallest then parent , Im happy  and stop bubbling up (climbing up is done)

            if self.heap[index] <= self.heap[parentIndex]:
                break
            # if i am bigger than a parent , then swap with parent and keep bubbling up

            self.heap[index] , self.heap[parentIndex] = (self.heap[parentIndex] ,self.heap[index]) # swap

            # move up to parent index or position and check again

            index = parentIndex  
    def display(self):
        print(self.heap)


    def delete(self):

        if not self.heap:
            return None
        
        if len(self.heap) ==1:
            return self.heap.pop()
        
        maximum = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.bubbleDown(0)

        return maximum

    

    def bubbleDown(self , index):

        size  = len(self.heap)

        while True:

            left =  2 * index + 1
            right = 2 * index + 2

            largest =index

            if left < size and self.heap[left] > self.heap[largest]:
                largest =left
            if right < size and self.heap[right] > self.heap[largest]:
                largest =right
            
            if largest == index:
                break

            self.heap[index], self.heap[largest] = (
                self.heap[largest],
                self.heap[index]
            )

            index = largest

    
    

heap = MaxHeap()

heap.insert(50)
heap.insert(30)
heap.insert(45)
heap.insert(10)
heap.insert(15)
heap.insert(20)
heap.insert(40)
heap.display()

heap.insert(60)


heap.display()

print("deleted:" ,heap.delete())
heap.display()