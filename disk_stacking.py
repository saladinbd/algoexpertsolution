def diskStacking(disks):
    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]

    for i in range(len(disks)):
        for j in range(i):
            new_height = heights[j] + disks[i][2]
            if is_smaller(disks[j], disks[i]) and new_height > heights[i]:
                heights[i] = new_height

    return build_sequence(disks, heights)


def is_smaller(a, b):
    return a[0] < b[0] and a[1] < b[1] and a[2] < b[2]


def build_sequence(disks, heights):
    sequence = []
    idx, height = max(enumerate(heights), key=lambda x: x[1])

    while height > 0:
        sequence.append(disks[idx])
        height = height - disks[idx][2]
        while idx >= 0 and heights[idx] != height:
            idx -= 1
    return list(reversed(sequence))


def main():
    item = [
      [2, 1, 2],
      [3, 2, 3],
      [2, 2, 8],
      [2, 3, 4],
      [1, 3, 1],
      [4, 4, 5]
    ]
    diskStacking(item)


if __name__ == '__main__':
    main()
