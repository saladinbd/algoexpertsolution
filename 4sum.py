
def four_sum(nums, target):
    return k_sum(4, sorted(nums), target)


def k_sum(index, array, target_sum):
    if index == 2 and len(array) >= 2:
        return two_sum(array, target_sum)

    sum_list = []
    i = 0
    while i < len(array):
        result = k_sum(index - 1, array[i + 1:], target_sum - array[i])
        if len(result) > 0:
            for j in result:
                sum_list.append([array[i]] + j)

        while i < len(array) - 1 and array[i + 1] == array[i]:
            i += 1

        i += 1

    return sum_list


def two_sum(nums, target):
    hash_map = []
    result = []
    i = 0
    while i < len(nums):
        value = target - nums[i]

        if value in hash_map:
            result.append([value, nums[i]])
            while (i < len(nums) - 1) and (nums[i] == nums[i + 1]):
                i += 1

        else:
            hash_map.append(nums[i])
        i += 1

    return result


def main():
    print(four_sum([1,0,-1,0,-2,2], 0))


if __name__ == '__main__':
    main()
