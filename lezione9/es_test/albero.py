# nodo in posizione 0 = radice
# nodo in posizione i = figlio a sinistra 2*i+1
#nodo in posizione i = figlio a destra 2*i+2
# figli sinistra sono gli indici dispari mentre a destra sono gli indici pari


def is_symmetric(tree: list[int]) -> bool:
    return are_mirrored(1,2)


def are_mirrored(tree: list[int], left_index: int, right_index: int):
    if left_index >= len(tree) or right_index >= len(tree):
        return True
    
    if tree[left_index]  != tree[right_index]:
        return False
    
    left_of_left =  2* left_index + 1
    right_of_left = 2* left_index + 2
    left_of_right = 2* right_index + 1
    right_of_right = 2* right_index + 2

    symmetric_extremes = are_mirrored(tree, left_of_left, right_of_right)
    symmetric_inner = are_mirrored(tree, right_of_left, left_of_right)
    return symmetric_extremes and symmetric_inner