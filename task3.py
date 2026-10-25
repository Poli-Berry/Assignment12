def my_sort(numbers):
    n = len(numbers)
    comparisons = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparisons += 1

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers, comparisons


# Test with 5 numbers
short_list = [5, 2, 4, 1, 3]
print("5 items:", my_sort(short_list))

# Test with 10 numbers
long_list = [10, 7, 3, 9, 1, 5, 8, 2, 6, 4]
print("10 items:", my_sort(long_list))

print("Comparisons for n items: n * (n-1) / 2")
