import time
import random

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Function to measure execution time
def measure_time(arr):
    start = time.perf_counter()
    insertion_sort(arr)
    end = time.perf_counter()
    return end - start


# Input sizes
sizes = [1000, 2000, 4000, 8000]

# File to store results
file =open("insertion_sort_analysis.txt", "w")

file.write("Insertion Sort Empirical Analysis\n")
file.write("----------------------------------\n")
file.write("Size\tBest Case\tAverage Case\tWorst Case\n")

print("Size\tBest\t\tAverage\t\tWorst")

for n in sizes:
    # Best Case (Already Sorted)
    best_case = list(range(n))
    best_time = measure_time(best_case.copy())

    # Average Case (Random)
    avg_case = random.sample(range(n), n)
    avg_time = measure_time(avg_case.copy())

    # Worst Case (Reverse Sorted)
    worst_case = list(range(n, 0, -1))
    worst_time = measure_time(worst_case.copy())

    print(f"{n}\t{best_time:.6f}\t{avg_time:.6f}\t{worst_time:.6f}")
    file.write(f"{n}\t{best_time:.6f}\t{avg_time:.6f}\t{worst_time:.6f}\n")

file.close()
