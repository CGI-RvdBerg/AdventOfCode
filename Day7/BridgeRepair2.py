from itertools import product, chain
from operator import mul, add, concat

with open("BridgeRepair_Data.txt") as file:
    count = 0
    for line in file.readlines():
        test_val, other_values = line.split(":")
        vals = [int(val) for val in other_values.strip().split(" ")]
        print(test_val)
        for permutation in product([add, mul, concat], repeat=len(vals) - 1):
            test_attempt = vals[0]
            for op, val in zip(permutation, vals[1:]):
                if op == concat:
                    test_attempt = int(op(str(test_attempt), str(val)))
                else:
                    test_attempt = op(test_attempt, val)
            if test_attempt == int(test_val):
                count += test_attempt
                break
print(count)
