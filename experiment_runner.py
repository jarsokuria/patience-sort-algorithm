import random
import time
from patience_sort import PatienceSort

sizes = [1,2,3,4,5,10,250,999,9999,89786]

for size in sizes:

    data = [random.randint(1,1000000) for _ in range(size)]

    sorter = PatienceSort(data)

    start = time.time()
    sorter.sort()
    end = time.time()

    print("List Size:", size)
    print("Comparisons:", sorter.comparisons)
    print("Swaps:", sorter.swaps)
    print("Execution Time:", end-start)
    print()
