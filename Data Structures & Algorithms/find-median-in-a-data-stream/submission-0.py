class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
# if large isnt empty, and x is greater than the smallest element in larger
# insert into large
# ow insert into small.
# if oneheap becomes larger than the other by more than 1; move top element into other heap
    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small, -1 * num)
            # max heaps arent normally implemented in python. we have to implement a minheap and keep pushing it to the element after the 
        
        # now we need to ensure that both heaps are no more than 1 element larger than the other list
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small) 
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) +1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large)> len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0])/ 2.0
        

# what do i do here right n ow
# i want to use the heap method 
# max heap - smaller half of numbers
#min heap - larger 
# o(log n) insert, o(1) median lookup
