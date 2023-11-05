class arr_sorting:
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

    def selection_sort(self):
        for ind in range(len(self.arr)):
            min_index = ind
    
            for j in range(ind + 1, len(self.arr)):
                # select the minimum element in every iteration
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            # swapping the elements to sort the array
            (self.arr[ind], self.arr[min_index]) = (self.arr[min_index], self.arr[ind])
        return self.arr
    
    def bubble_sort(self):
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

"""
sort_array = sorting([64, 34, 25, 12, 22, 11, 90])
print("Insertion sort: ", sort_array.insertion_sort())
print("Selection sort: ", sort_array.selection_sort())
print("Bubble sort: ", sort_array.bubbleSort())
"""





