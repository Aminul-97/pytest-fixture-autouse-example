import sqlite3

class sorting:
    def __init__(self, array: int) -> None:
        self.arr = array
    
    def insertion_sort(self):
       for i in range(1, len(self.arr)):
 
        key = self.arr[i]
 
        j = i-1
        while j >= 0 and key < self.arr[j] :
                self.arr[j + 1] = self.arr[j]
                j -= 1
        self.arr[j + 1] = key
        return self.arr

    def merge_sort(self):
        if len(self.arr) > 1:
    
            mid = len(self.arr)//2
    
            L = self.arr[:mid]
    
            R = self.arr[mid:]
    
            self.mergeSort(L)
    
            self.mergeSort(R)
    
            i = j = k = 0
    
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    self.arr[k] = L[i]
                    i += 1
                else:
                    self.arr[k] = R[j]
                    j += 1
                k += 1
    
            # Checking if any element was left
            while i < len(L):
                self.arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                self.arr[k] = R[j]
                j += 1
                k += 1 
        return self.arr
    
    def bubbleSort(self):
        n = len(self.arr)
        
        # Traverse through all array elements
        for i in range(n):
            swapped = False
    
            for j in range(0, n-i-1):
    
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swapped = True
            if (swapped == False):
                break

        return self.arr

sort_array = sorting([64, 34, 25, 12, 22, 11, 90])
print(sort_array.insertion_sort())
print(sort_array.merge_sort())
print(sort_array.bubbleSort())






