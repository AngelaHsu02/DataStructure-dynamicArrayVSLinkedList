import random
import time


class Object:
    def __init__(self, num, foo):
        self.num = random.randint(0, 9999)
        self.foo = [0] * foo
        self.next = None  # pointer


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def addListObject(self, num, foo):
        for n in range(num):
            obj = Object(num, foo)
            if self.head is None:
                self.head = obj
            else:
                self.tail.next = obj
            self.tail = obj
        return linkedList

    def sum(self, linkedList):
        sum = 0
        for node in linkedList:
            sum += node.num
        return sum

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            node = self.current
            self.current = self.current.next
            return node


if __name__ == '__main__':
    numList = [2**n for n in range(10, 31)]
    # numList = [2**n for n in range(1, 3)]
    fooList = [1, 7, 63, 511]
    # fooList = [1, 7]
    numTrials = 10  # 測量10次，避免outliers

    for n in numList:
        for k in fooList:
            totalAddTime = 0
            totalSumTime = 0
            for i in range(numTrials):
                linkedList = SingleLinkedList()
                startTime = time.time()
                linkedList.addListObject(n, k)
                # print(f"Linked List: {n}objs, 1num,{k}foo")
                # for node in linkedList:
                #    print(f"num: {node.num}, foo: {node.foo}")
                endTime = time.time()
                totalAddTime += endTime - startTime

                startTime = time.time()
                linkedList.sum(linkedList)
                # print(linkedList.sum(linkedList))
                endTime = time.time()
                totalSumTime += endTime - startTime

            averageAddTime = totalAddTime / numTrials
            averageSumTime = totalSumTime / numTrials
            # print(f"Linked List: {n}objs, {k}foo, Average Add time: {averageAddTime} seconds, Average Sum time: {averageSumTime} seconds")
            print(f'{n}, {k}, {averageAddTime}, {averageSumTime}')
