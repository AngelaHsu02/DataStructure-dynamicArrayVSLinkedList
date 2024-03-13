import random
import time


class dynamicArray:
    def __init__(self, foo):
        self.num = random.randint(0, 9999)
        self.foo = [0] * foo

    # def generate(self, num, foo):
    #     darray=[]
    #     # obj = dynamicArray(foolength)
    #     for n in range(num): #可加測新增obj甚麼時候會最久
    #         obj = dynamicArray(foo) #創不必要的物件->開在迴圈中才會每次生成不同的num
    #         darray.append(obj)
    #     return darray

    def generate(self, num, foo):
        return [dynamicArray(foo) for n in range(num)]

    def sum(self, n):
        # numsum = 0
        # for obj in darray:
        #     numsum += obj.num
        # # # print(f"加總2^{i}個num: {numsum}")
        # return numsum
        # return sum(obj.num for obj in darray)
        numsum = 0
        for i in range(n):
            numsum += darray[i].num
        return (numsum)


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
            da = dynamicArray(n)
            for i in range(numTrials):

                start_gen = time.time()
                darray = da.generate(n, k)
                # print(f"Dynamic Array: {n}objs, 1num,{k}foo")
                # for obj in darray:
                #    print(f"num: {obj.num}, foo: {obj.foo}")
                # print(darray[1].num)
                end_gen = time.time()
                totalAddTime += end_gen-start_gen

                start_sum = time.time()
                da.sum(n)
                # print(da.sum(n))
                end_sum = time.time()
                totalSumTime += end_sum-start_sum

            averageAddTime = totalAddTime / numTrials
            averageSumTime = totalSumTime / numTrials
            print(f"{n}, {k}, {averageAddTime}, {averageSumTime}")
