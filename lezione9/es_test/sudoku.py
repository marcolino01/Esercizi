def sudoku(tavola : list[list[int]]) -> bool:
    rows: dict[int, list[int]] = {i:[] for i in range(9)}
    cols: dict[int, list[int]] = {i:[] for i in range(9)}
    squares : dict[int, list[int]] = {i:[] for i in range(9)}

    for i in range(9):
        for j in range(9):
            curr_elem: str = tavola[i],[j]
            if curr_elem != ".":
                i_square, j_square = i // 3, j // 3
                square_index = i_square + 3*j_square
                if curr_elem in rows[i]:
                    return False
                if curr_elem in cols[j]:
                    return False
                if curr_elem in squares[square_index]:
                    return False
                
                rows[i].append(curr_elem)
                cols[j].append(curr_elem)
    return False
