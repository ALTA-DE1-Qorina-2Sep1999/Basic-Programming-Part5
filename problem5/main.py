def pair_sum(numbers, target):
    assert numbers
    left = 0
    right = len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return None

if __name__ == '__main__':
    print(pair_sum([1, 2, 3, 4, 6], 6)) # [1, 3]
    print(pair_sum([2, 5, 9, 11], 11)) # [0, 2]
    print(pair_sum([1, 3, 5, 7], 12)) # [2, 3]
    print(pair_sum([1, 4, 6, 8], 10)) # [1, 2]
    print(pair_sum([1, 5, 6, 7], 6)) # [0, 1]
    print(pair_sum([1, 2, 3, 4, 6], 11)) # None