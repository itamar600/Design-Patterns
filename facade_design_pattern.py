class Array:
    def __init__(self):
        self.capacity = 2  # Initial capacity of the array
        self.length = 0  # Number of elements currently in the array
        self.arr = [0] * self.capacity  # Array of capacity = 2
    
    def push_back(self, n):
        """Append an element to the end of the array."""
        if self.length == self.capacity:  # Check if the array is full
            self.resize()  # If full, resize the array
        self.arr[self.length] = n  # Add the new element to the end of the array
        self.length += 1  # Increment the length
    
    def resize(self):
        """Resize the array to double its current capacity."""
        self.capacity = 2 * self.capacity  # Double the capacity
        newArr = [0] * self.capacity  # Create a new array with the new capacity
        for i in range(self.length):
            newArr[i] = self.arr[i]  # Copy elements from the old array to the new one
        self.arr = newArr  # Update the array reference to the new array
