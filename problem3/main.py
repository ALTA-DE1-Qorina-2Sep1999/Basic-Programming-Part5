def join_array_remove_duplicate(arrayA, arrayB):
    merged = arrayA + arrayB
    result = []

    for item in merged:
        if item not in result:
            result.append(item)

    return result

if __name__ == '__main__':
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"])) # ["apel", "anggur", "lemon", "leci", "nanas"]
    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"])) # ["samsung", "apple", "sony", "xiaomi"]
    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"])) # ["football", "basketball"]
    print(join_array_remove_duplicate(["apple", "banana"], []))
    print(join_array_remove_duplicate(["apple", "banana", "banana", "cherry"], ["cherry", "date", "date"]))