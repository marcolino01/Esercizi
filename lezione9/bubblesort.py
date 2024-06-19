def bubble_sort(x: list[int]):

    ho_fatto_swap : bool = False
    for i in range(len(x)):
        for j in range(len(x) -i - 1):                      # -i per fare meno iterazioni per non controllare gli elementi che ho swappato
            if x[j] > x[j+1]:
                ho_fatto_swap = True
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
            if not ho_fatto_swap:
                break
    

l : list[int] = [9321, 0, 2831, 12, 3, 4, 5]
bubble_sort(l)
print(l)
    
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
