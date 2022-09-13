def maximizeExpression(array):
    if len(array) < 4:
        return 0

    maxA = [float("-inf") for _ in array]
    maxAB = [float("-inf") for _ in array]
    maxABC = [float("-inf") for _ in array]
    maxABCD = [float("-inf") for _ in array]

    for i, num in enumerate(array):
        if i == 0:
            maxA[i] = num
        else:
            maxA[i] = max(maxA[i-1], num)

        if i >= 1:
            maxAB[i] = max(maxAB[i-1], maxA[i-1] - num)

        if i >= 2:
            maxABC[i] = max(maxABC[i-1], maxAB[i-1] + num)

        if i >= 3:
            maxABCD[i] = max(maxABCD[i-1], maxABC[i-1] - num)

    return maxABCD[-1]


def main():
    array = [3, 6, 1, -3, 2, 7]
    print(maximizeExpression(array))


if __name__ == '__main__':
    main()
