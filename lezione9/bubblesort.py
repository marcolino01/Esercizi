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
    