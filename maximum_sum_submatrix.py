def submatrix_total(matrix, r_start, c_start, size):
    total = 0
    for r in range(r_start, r_start + size):
        total += sum(matrix[r][c_start:(c_start + size)])

    return total



def maximumSumSubmatrix(matrix, size):

    max_sum = float("-inf")

    for r in range(len(matrix) - size + 1):
        for c in range(len(matrix[0]) - size + 1):
            sub_total = submatrix_total(matrix, r, c, size)
            max_sum = max(max_sum, sub_total)

    return max_sum if max_sum != float("-inf") else -1


def main():
    matrix = [
      [5, 3, -1, 5],
      [-7, 3, 7, 4],
      [12, 8, 0, 0],
      [1, -8, -8, 2]
    ]
    size = 2
    print(maximumSumSubmatrix(matrix, size))


if __name__ == '__main__':
    main()
