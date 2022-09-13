def helper(pi, numbers, memoize):
    if len(pi) == 0:
        return 0

    if pi not in memoize:
        mins = float("inf")
        for i in range(len(pi)):
            if pi[:i+1] in numbers:
                mins = min(mins, helper(pi[i+1:], numbers, memoize))
        memoize[pi] = mins + 1

    return memoize[pi]


def numbersInPi(pi, numbers):
    memoize = {}
    result = helper(pi, numbers, memoize) - 1

    return -1 if result == float("inf") else result


def main():
    pi = "3141592653589793238462643383279"
    numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]

    numbersInPi(pi, numbers)


if __name__ == '__main__':
    main()
