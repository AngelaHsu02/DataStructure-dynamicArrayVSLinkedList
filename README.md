## 目標
比較dynamic array與linked list新增、加總的執行時間，並討論cache的影響。

Compare the execution time for adding and summing operations in dynamic arrays and linked lists, and discuss the impact of caching.
## 方法
測量新增、加總𝑛 = 2ℎ(ℎ = 10, 11, 12, …, 30)個object所需時間，報告實驗數據來自dynamicArray.py, linkedList.py。

Measure the time required to add and sum 𝑛 = 2ℎ(ℎ = 10, 11, 12, …, 30) objects. Report experimental data derived from dynamicArray.py and linkedList.py.
## 結論
1.新增linked list快，因為pointer可以接到新增的數字上，但array新增時，後面幾乎所有格子都要往後移動。

2.加總array快，因為array是連續型，可以直接和cache拿不用再到RAM。

1.Adding elements to a linked list is faster because pointers can be directly linked to the new numbers. However, when adding to an array, almost all the subsequent elements have to be shifted.

2.Summing elements in an array is faster because arrays are contiguous, allowing direct retrieval from the cache without the need to access RAM again.
