VALUE_IDX = 0
ITEMS_IDX = 1


def knapsackProblem(items, capacity):
    DP = [[[0, []] for j in range(capacity + 1)] for i in range(len(items) + 1)]

    for idx, item in enumerate(items):
        value, weight = item
        dp_i = idx + 1

        for c in range(capacity + 1):
            if c >= weight:
                if DP[dp_i - 1][c][VALUE_IDX] > DP[dp_i][c - weight][VALUE_IDX] + value:
                    DP[dp_i][c] = DP[dp_i - 1][c]
                else:
                    DP[dp_i][c][VALUE_IDX] = DP[dp_i - 1][c - weight][VALUE_IDX] + value
                    DP[dp_i][c][ITEMS_IDX] = DP[dp_i - 1][c - weight][ITEMS_IDX] + [idx]
            else:
                DP[dp_i][c] = DP[dp_i - 1][c]

    return DP[-1][-1]


def main():
    item = [
      [1, 2],
      [4, 3],
      [5, 6],
      [6, 7]
    ]
    capacity = 10
    knapsackProblem(item, capacity)


if __name__ == '__main__':
    main()
