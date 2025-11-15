"""
This program takes a list of numbers, sorts them using a simple sorting method,
and then finds the median.

It follows the exact pseudocode:
- First sort the list
- Then check if the length is even or odd
- Return the correct median value
"""

from typing import List


def sort_numbers(numbers: List[float]) -> None:
    """
    A simple sorting function that uses 'selection sort'.

    What selection sort does:
    - Look through the list to find the smallest number
    - Put that number in the first position
    - Then find the next smallest number and put it in the second position
    - Keep doing this until the list is sorted

    This function changes the original list.
    """
    n = len(numbers)

    for i in range(n):
        # Assume the current position has the smallest value
        min_index = i

        # Look through the rest of the list to find an even smaller number
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        # If a smaller number was found, swap it into the correct position
        if min_index != i:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]


def sort_and_find_median(numbers: List[float]) -> float:
    """
    Sort the list of numbers, then calculate the median.

    Median explanation:
    - If the list has an odd number of items: the middle value is the median
    - If the list has an even number of items: median is the average of the two middle values
    """
    if not numbers:
        raise ValueError("Cannot find the median of an empty list.")

    # Sort the list first (as required by the pseudocode)
    sort_numbers(numbers)
    n = len(numbers)

    # If the number of items is even
    if n % 2 == 0:
        left_middle = numbers[n // 2 - 1]
        right_middle = numbers[n // 2]
        return (left_middle + right_middle) / 2

    # If the number of items is odd, return the middle number
    else:
        return numbers[n // 2]

def main():
    """
    Simple user interface:
    - Asks the user to type numbers separated by spaces
    - Converts them into a list of floats
    - Prints the sorted list and the calculated median
    """
    print("Median Calculator (using a custom sorting function)")
    print("Type numbers separated by spaces, for example: 10 2 5 7 1")

    raw = input("Numbers: ").strip()

    if not raw:
        print("No input entered.")
        return

    try:
        # Convert the user's text into a list of numbers
        nums = [float(x) for x in raw.split()]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        return

    median = sort_and_find_median(nums)
    print(f"Sorted numbers: {nums}")
    print(f"Median: {median}")


if __name__ == "__main__":
    main()
