import random

class PatienceSort:

    def __init__(self, arr):
        self.arr = arr
        self.piles = []
        self.comparisons = 0
        self.swaps = 0

    def sort(self):

        # Phase 1: Build piles
        for card in self.arr:
            placed = False

            for pile in self.piles:
                self.comparisons += 1

                if pile[-1] >= card:
                    pile.append(card)
                    self.swaps += 1
                    placed = True
                    break

            if not placed:
                self.piles.append([card])
                self.swaps += 1

        # Phase 2: Collect elements
        sorted_list = []

        while any(self.piles):

            min_val = float("inf")
            min_index = -1

            for i, pile in enumerate(self.piles):

                if pile:
                    self.comparisons += 1

                    if pile[-1] < min_val:
                        min_val = pile[-1]
                        min_index = i

            sorted_list.append(self.piles[min_index].pop())
            self.swaps += 1

        return sorted_list


if __name__ == "__main__":

    numbers = [8, 3, 5, 2, 9, 1]

    sorter = PatienceSort(numbers)
    result = sorter.sort()

    print("Original List:", numbers)
    print("Sorted List:", result)
    print("Comparisons:", sorter.comparisons)
    print("Swaps:", sorter.swaps)
