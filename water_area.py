def water_area(heights):
    maxes = [0 for x in heights]
    left_max = 0

    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = left_max
        left_max = max(left_max, height)

    right_max = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        min_height = min(right_max, maxes[i])
        if height < min_height:
            maxes[i] = min_height - height
        else:
            maxes[i] = 0
        right_max = max(right_max, height)

    return sum(maxes)


def main():
    water_area([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3])


if __name__ == '__main__':
    main()
