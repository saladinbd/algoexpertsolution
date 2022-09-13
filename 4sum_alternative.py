
def four_sum(nums, target):
    return k_sum(4, sorted(nums), target)


def k_sum(index, array, target_sum):
    if not array:
        return []

    if index == 2 and len(array) >= 2:
        return two_sum(array, target_sum)

    average_value = target_sum // index
    if average_value < array[0] or array[-1] < average_value:
        return []

    sum_list = []
    for i in range(len(array)):
        if i != 0 and array[i] == array[i - 1]:
            continue

        result = k_sum(index - 1, array[i + 1:], target_sum - array[i])
        if len(result) > 0:
            for j in result:
                sum_list.append([array[i]] + j)

    return sum_list


def two_sum(nums, target):
    res = []
    s = set()

    for i in range(len(nums)):
        if len(res) == 0 or res[-1][1] != nums[i]:
            if target - nums[i] in s:
                res.append([target - nums[i], nums[i]])
        s.add(nums[i])

    return res


def main():
    print(four_sum([1,0,-1,0,-2,2], 0))


if __name__ == '__main__':
    main()
