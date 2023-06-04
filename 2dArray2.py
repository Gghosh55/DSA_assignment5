def count_complete_rows(n):
    complete_rows = 0
    row_number = 1

    while n >= row_number:
        complete_rows += 1
        n -= row_number
        row_number += 1

    return complete_rows
n = 5

print(count_complete_rows(n))
