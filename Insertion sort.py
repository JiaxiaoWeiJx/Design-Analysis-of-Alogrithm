import numpy as np
import timeit
import random
import matplotlib.pyplot as plt

def insertion_sort(A):
    n = len(A);
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


# Example usage:
A = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(A)

print("Sorted array:", A)

# Benchmark time for the given array
if __name__ == "__main__":
    setup_code = "from __main__ import insertion_sort"

    # Measure the time taken to execute the insertion_sort function
    time_taken = timeit.timeit(stmt="insertion_sort({})".format(A), setup=setup_code, number=1000)

    print("Time taken: {:.6f} seconds".format(time_taken))

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def benchmark_insertion_sort(size):
    setup_code = "from __main__ import insertion_sort"
    input_data = generate_random_array(size)

    #print("Original Array (size={}): {}".format(size, input_data))

    time_taken = timeit.timeit(stmt="insertion_sort({})".format(input_data), setup=setup_code, number=100)

    sorted_array = list(input_data)  # Create a copy to avoid modifying the original array
    insertion_sort(sorted_array)

    #print("Sorted Array (size={}): {}".format(size, sorted_array))

    return time_taken

if __name__ == "__main__":
    array_sizes = [100, 500, 1000, 2000, 5000]  # List of different array sizes to test
    benchmark_times = []

    for size in array_sizes:
        time_taken = benchmark_insertion_sort(size)
        benchmark_times.append(time_taken)

        print("Array size: {}, Time taken: {:.6f} seconds".format(size, time_taken))


# Plot the results
plt.plot(array_sizes, benchmark_times, marker='o')
plt.title('Insertion Sort Benchmark')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.savefig("Insertion_benchmark.png")
plt.show()