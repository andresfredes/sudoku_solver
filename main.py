START = [
    [0, 0, 0, 0, 0, 8, 0, 2, 0],
    [0, 6, 2, 0, 3, 0, 0, 0, 4],
    [0, 8, 0, 6, 2, 0, 1, 0, 0],
    #
    [9, 2, 3, 0, 8, 5, 0, 0, 0],
    [5, 1, 8, 0, 0, 0, 9, 3, 7],
    [0, 0, 0, 1, 9, 0, 2, 5, 8],
    #
    [0, 0, 7, 0, 1, 9, 0, 6, 0],
    [2, 0, 0, 0, 6, 0, 3, 7, 0],
    [0, 4, 0, 5, 0, 0, 0, 0, 0],
]

NEW = [
    [0, 3, 0, 0, 0, 0, 0, 0, 4],
    [1, 0, 7, 0, 0, 0, 5, 0, 0],
    [0, 6, 2, 0, 0, 0, 0, 0, 0],
    #
    [0, 0, 0, 0, 5, 8, 3, 1, 0],
    [4, 0, 0, 7, 6, 2, 0, 0, 8],
    [0, 7, 8, 1, 9, 0, 0, 0, 0],
    #
    [0, 0, 0, 0, 0, 0, 6, 4, 0],
    [0, 0, 6, 0, 0, 0, 7, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 2, 0],
]

total = 0


def brute_force_solver(nested: list[list]):
    global total
    print(f"Solve attempt {total}")
    total += 1
    if available_location(nested) is None:
        return nested
    temp = [x for x in [y.copy() for y in nested]]
    for i, row in enumerate(temp):
        for j, col in enumerate(row):
            if col != 0:
                continue
            for num in range(1, len(nested) + 1):
                if not valid_position(temp, i, j):
                    continue
                temp[i][j] = num
                solution = backtrack_solver(temp)
                if solution is not None:
                    return solution

    return None


def backtrack_solver(nested: list[list]):
    next_pos = available_location(nested)
    if next_pos is None:
        return nested
    for i in range(1, 10):
        if valid_position(nested, i, next_pos[0], next_pos[1]):
            nested[next_pos[0]][next_pos[1]] = i
            print(f"Trying {i} at [{next_pos[0]}, {next_pos[1]}]")
            solution = backtrack_solver(nested)
            if solution is not None:
                return solution
            print("Backtracking...")
            nested[next_pos[0]][next_pos[1]] = 0
    return None


def valid_position(nested: list[list], num, row_index, col_index):
    if num in nested[row_index]:
        return False
    if num in column(nested, col_index):
        return False
    if num in local_square(nested, row_index, col_index):
        return False
    return True


def available_location(nested: list[list]):
    for i, row in enumerate(nested):
        for j, col in enumerate(row):
            if col == 0:
                return i, j
    return None


def column(nested: list[list], column_index):
    return map(lambda sublist: sublist[column_index], nested)


def local_square(nested: list[list], row_index, column_index):
    x = slice_index(row_index)
    y = slice_index(column_index)
    flat = set([])
    for row in nested[x : x + 3]:
        for num in row[y : y + 3]:
            flat.add(num)
    return flat


def slice_index(val):
    return (val // 3) * 3


def main(nested: list[list]):
    solution = backtrack_solver(nested)
    print(solution)


if __name__ == "__main__":
    main(NEW)
