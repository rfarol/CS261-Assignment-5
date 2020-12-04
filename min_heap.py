# Course: CS261 - Data Structures
# Assignment: 5
# Student: Ryan Farol
# Description: Min heap class has multiple functions that allows you to add, get min, remove min, and build a min heap.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """adds a node to the minheap while keeping it in order. The following procedure was taken from the Heap
        Implementation lecture for A5."""
        self.heap.append(node) # add node to the end of the array
        if self.heap.length() == 1: # if there is only one element, then return
            return
        else:
            child_index = self.heap.length() - 1 # initialize index of child
            child_value = self.heap.get_at_index(child_index) # initialize value of child
            parent_index = (child_index - 1) // 2 # find child's parent index. Formula was taken from lecture
            parent_value = self.heap.get_at_index(parent_index) # get value of parent index

            # iterate throughout the array until index is 0. First, it checks if parent value is larger than child value
            while child_index != 0 and parent_value > child_value:
                self.heap.swap(child_index, parent_index) # swap if larger
                child_index = parent_index # switch indexes
                parent_index = (child_index - 1) // 2 # find new parent index from current index
                parent_value = self.heap.get_at_index(parent_index) # get the value of new parent index
            return


    def get_min(self) -> object:
        """returns an object with the minumum key without removing it from the heap. If empty, an exception is raised.
        Since the add function already sorts the minheap, index 0 will be returned"""
        if self.heap.length() == 0:
            return MinHeapException
        else:
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """function returns an object with a minumum key and removes it from the heap. If the heap is empty,
        exception is raised. The following procedure was taken from the Heap Implementation lecture for A5 """
        if self.heap.length() == 0: # if array is empty, raise exception
            return MinHeapException
        if self.heap.length() == 1: # if array just contains one element, remove it and return the value
            return self.heap.pop()
        else:
            self.heap.swap(0, self.heap.length() - 1) # swap the last value and first value
            return_value = self.heap.pop() # pop the end of the list and store in variable
            replace_index = 0 # initialize parent index at the top of the min heap
            replace_value = self.heap.get_at_index(replace_index) # initialize the value of parent index
            while replace_index < self.heap.length(): # iterate throughout the min heap starting at the top of the heap
                left_child_index = (2 * replace_index) + 1 # calculate index of potential left child
                right_child_index = (2 * replace_index) + 2 # calculate index of potential right child

                if left_child_index < self.heap.length(): # checks if left child index is within the min heap
                    left_child_value = self.heap.get_at_index(left_child_index) # if within min heap, initialize value
                else:
                    left_child_value = None # if not, then initialize as None

                if right_child_index < self.heap.length(): # checks if right child index is within the min heap
                    right_child_value = self.heap.get_at_index(right_child_index) # if within min heap, initialize value
                else:
                    right_child_value = None # if not, then initialize as None

                # if both right and left children exists, compare both left and right children and traverse down the
                # lower value of the two children
                if right_child_value != None and left_child_value != None:
                    if left_child_value < right_child_value: # if left child value is less, traverse down the left side
                        min_value = left_child_value
                        min_index = left_child_index
                    elif right_child_value < left_child_value: # if right child value is less, traverse down the left side
                        min_value = right_child_value
                        min_index = right_child_index

                # if only left child exists, traverse down the left side
                elif left_child_value != None and right_child_value == None:
                    min_value = left_child_value
                    min_index =left_child_index

                # if only left child exists, traverse down the right side
                elif right_child_value != None and left_child_value == None:
                    min_value = right_child_value
                    min_index = right_child_index
                else: # if left and right child don't exist, return value
                    return return_value

                # checks if replacement value needs to swap with the child. If greater, swap
                if replace_value > min_value:
                    self.heap.swap(replace_index, min_index)
                    replace_index = min_index
                    replace_value = self.heap.get_at_index(replace_index)
                else:
                    return return_value # return value


    def build_heap(self, da: DynamicArray) -> None:
        """function receives a dynamic array with objects in any order and builds a proper MinHeap from them.
        The following procedure was taken from the Heap Implementation lecture for A5."""
        new_DA = DynamicArray() # new dynamic array is created
        for i in range(da.length()): # move all elements into new array
            new_DA.append(da.get_at_index(i))

        self.heap = new_DA # set heap to new array
        if self.heap.length() == 1: # if heap contains only one element, return
            return
        if self.heap.length() == 0: # if empty, raise exception
            raise MinHeapException
        counter = self.heap.length() - 1 # set counter to the full length of the array
        while counter != 0: # iterate throughout the array until the first index
            parent_index = counter
            parent_node = self.heap.get_at_index(parent_index)
            while parent_index < self.heap.length():
                left_child_index = (2 * parent_index) + 1  # calculate index of potential left child
                right_child_index = (2 * parent_index) + 2  # calculate index of potential right child

                if left_child_index < self.heap.length():  # checks if left child index is within the min heap
                    left_child_value = self.heap.get_at_index(left_child_index)  # if within min heap, initialize value
                else:
                    left_child_value = None  # if not, then initialize as None

                if right_child_index < self.heap.length():  # checks if right child index is within the min heap
                    right_child_value = self.heap.get_at_index(
                        right_child_index)  # if within min heap, initialize value
                else:
                    right_child_value = None  # if not, then initialize as None

                # if both right and left children exists, compare both left and right children and traverse down the
                # lower value of the two children
                if right_child_value != None and left_child_value != None:
                    if left_child_value < right_child_value:  # if left child value is less, traverse down the left side
                        min_value = left_child_value
                        min_index = left_child_index
                    elif right_child_value < left_child_value:  # if right child value is less, traverse down the left side
                        min_value = right_child_value
                        min_index = right_child_index

                # if only left child exists, traverse down the left side
                elif left_child_value != None and right_child_value == None:
                    min_value = left_child_value
                    min_index = left_child_index

                # if only left child exists, traverse down the right side
                elif right_child_value != None and left_child_value == None:
                    min_value = right_child_value
                    min_index = right_child_index
                else:  # if left and right child don't exist, break while loop
                    break

                # checks if parent value needs to swap with the child. If greater, swap
                if parent_node > min_value:
                    self.heap.swap(parent_index, min_index)
                    parent_index = min_index
                    replace_value = self.heap.get_at_index(parent_index)
                else:
                    break
            counter -= 1 # decrement while loop by 1




# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
