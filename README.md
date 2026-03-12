Name: IAN KURIA JARSO 
Registration Number: EB3/67584/23

Algorithm Used
Patience Sort

Description
This project implements the Patience Sort algorithm without using built-in sorting functions. The program sorts an unsorted list of integers while tracking the number of comparisons and swaps performed.

How the Algorithm Works
Patience Sort works by creating piles of numbers similar to the card game solitaire. Each number is placed on the leftmost pile whose top element is greater than or equal to it. If no such pile exists, a new pile is created.

After all numbers are placed into piles, the algorithm repeatedly selects the smallest top element among the piles until the sorted list is produced.

Time Complexity
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)

Space Complexity
O(n)

Experiment
The algorithm was tested using lists with sizes:
1, 2, 3, 4, 5, 10, 250, 999, 9999, 89786, 789300, and 1,780,000 elements.

Results showed that execution time and comparisons increased with input size but followed the expected O(n log n) pattern.
