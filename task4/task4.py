import sys
import numpy as np


def min_moves(nums):
    med = np.median(nums)
    moves = sum(abs(num - med) for num in nums)
    
    return moves


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
            nums = []
            for line in file:
                nums.append(int(line))
    print("Минимальное количество ходов:", min_moves(nums))

