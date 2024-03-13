import random
import time
import ctypes


class Object:
    def __init__(self, foo):
        self.num = random.randint(0, 9999)
        self.foo = [0] * foo


class DynamicArray(object):
    def __init__(self):
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 1  # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements stored in array
        """
        return self.n

    def __getitem__(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            # Check it k index is in bounds of array
            return IndexError('K is out of bounds !')

        return self.A[k]  # Retrieve from the array at index k

    def append(self, num, foo):
        """
        Add element to end of the array
        """
        for l in range(num):
            obj = Object(foo)
            if self.n == self.capacity:
                self._resize(2 * self.capacity)

            self.A[self.n] = obj  # Set self.n index to element
            self.n += 1
        return self.A

    def _resize(self, new_cap):
        """
        Resize internal array to capacity new_cap
        """
        B = self.make_array(new_cap)  # New bigger array

        for k in range(self.n):  # Reference all existing values
            B[k] = self.A[k]

        self.A = B  # Call A the new bigger array
        self.capacity = new_cap  # Reset the capacity

    def make_array(self, new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()

    def sum(self, n):
        numsum = 0
        for i in range(n):
            numsum += darray[i].num
        return numsum


if __name__ == '__main__':
    numList = [2**n for n in range(10, 31)]
    # numList = [2**n for n in range(1, 3)]
    fooList = [1, 7, 63, 511]
    # fooList = [1, 7]
    numTrials = 10
    for n in numList:
        for k in fooList:
            totalAddTime = 0
            totalSumTime = 0
            for i in range(numTrials):
                arr = DynamicArray()
                startTime = time.time()
                darray = arr.append(n, k)
                # print(f"Dynamic Array: {n}objs, 1num,{k}foo")
                # for obj in darray:
                #    print("num:", obj.num, "foo:", obj.foo)
                # print(darray[0].num, darray[0].foo)
                endTime = time.time()
                totalAddTime += endTime - startTime

                start_sum = time.time()
                arr.sum(n)
                end_sum = time.time()
                totalSumTime += end_sum-start_sum

            averageAddTime = totalAddTime / numTrials
            averageSumTime = totalSumTime / numTrials
            print(f"{n}, {k}, {averageAddTime}, {averageSumTime}")
