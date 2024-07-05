import time
import matplotlib.pyplot as plt

def mergesort(list_input: list[int])-> list[int]:
    if len(list_input) == 1:
        return list_input
    mid_point = len(list_input) // 2

    left_list : list[int] = mergesort(list_input=list_input[: mid_point])    #escluso il mid_point
    right_list : list[int] = mergesort(list_input=list_input[mid_point :])

    result : list[int] = merge(left_list, right_list)
    return result


def merge(list1 : list[int], list2 : list[int])-> list[int]:

    i, j = 0, 0

    result: list[int] = [None for _ in range(len(list1 + list2))]

    for k in range(len(result)):
        if list1[i] > list2[j]:
            result[k] = list2[j]
            j += 1
            if j == len(list2):
                
                return result[:k+1] + list1[i:]
        else:
            result[k] = list1[i]
            i += 1
            if i == len(list1):
                
                return result[:k+1] + list2[j:]


def bubble_sort_v2(x: list[int]):
    # Ω(n) -> caso migliore quando la lista è già ordinata
    # O(n^2) -> caso peggiore
    ho_fatto_swap: bool = True
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                # swap(x[j], x[j+1])
                ho_fatto_swap = False
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
        if ho_fatto_swap:
            break    



if __name__ == "__main__":
    import random

    MergeSort_times : list[float] = []
    BubbleSort_times : list[float] = []
    cases = [10, 50, 100, 250, 500, 1000, 2000, 5000, 10000, 20000, 30000, 40000]
    for n in [10, 50, 100, 250, 500, 1000, 2000, 5000, 10000, 20000, 30000, 40000]:
        list_input: list[int] = [random.randint(0, 10000) for _ in range(n)]
        start = time.time()
        result : list[int] = mergesort(list_input=list_input)
        end = time.time()
        MergeSort_times.append(end-start)

        start = time.time()
        result : list[int] = bubble_sort_v2(x = list_input) 
        end = time.time()
        BubbleSort_times.append(end-start)
    print(f"Merge: {MergeSort_times}\n Bubble {BubbleSort_times}")

    plt.plot(cases, MergeSort_times, label = 'Merge')
    plt.show(cases, BubbleSort_times, label = 'Bubble')

print("Ciuao")



