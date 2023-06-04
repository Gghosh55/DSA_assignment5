def find_original_array(changed):
    changed.sort()
    original = []

    for num in changed:
        half_num = num // 2

        if half_num in changed:
            changed.remove(half_num)
            original.append(half_num)
        else:
            return []

    return original
changed = [1, 3, 4, 2, 6, 8]

print(find_original_array(changed))
