def bubble_sort(arr):
    # Work on a copy so we sort in-place on the copy without modifying original test data directly
    a = list(arr)
    n = len(a)
    comparisons = 0
    swaps = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        # Early-exit optimization: stop if no swaps occurred in a full pass
        if not swapped:
            break

    return a, comparisons, swaps

def selection_sort(arr):
    a = list(arr)
    n = len(a)
    comparisons = 0
    swaps = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1

    return a, comparisons, swaps

def insertion_sort(arr):
    a = list(arr)
    n = len(a)
    comparisons = 0
    shifts = 0

    for i in range(1, n):
        key = a[i]
        j = i - 1

        # Shift elements of a[0..i-1] that are greater than key to one position ahead
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key

    return a, comparisons, shifts

# --- Driver Program ---
if __name__ == "__main__":
    test_cases = {
        "A. Random": [29, 10, 14, 37, 13, 5, 22],
        "B. Already sorted": [1, 2, 3, 4, 5, 6, 7],
        "C. Reverse sorted": [7, 6, 5, 4, 3, 2, 1],
        "D. Duplicates": [4, 2, 4, 1, 2, 3, 1],
        "E. Edge - Empty": [],
        "E. Edge - Single": [42],
        "E. Edge - Two Elements": [2, 1]
    }

    for name, input_arr in test_cases.items():
        print(f"=== Case: {name} | Input: {input_arr} ===")

        # Bubble Sort
        b_sorted, b_comp, b_swaps = bubble_sort(input_arr)
        print(f"Bubble Sort    -> Sorted: {b_sorted} | Comparisons: {b_comp}, Swaps: {b_swaps}")

        # Selection Sort
        s_sorted, s_comp, s_swaps = selection_sort(input_arr)
        print(f"Selection Sort -> Sorted: {s_sorted} | Comparisons: {s_comp}, Swaps: {s_swaps}")

        # Insertion Sort
        i_sorted, i_comp, i_shifts = insertion_sort(input_arr)
        print(f"Insertion Sort -> Sorted: {i_sorted} | Comparisons: {i_comp}, Shifts: {i_shifts}")
        print("-" * 65)
