import numpy as np

sorted_data = np.sort(np.loadtxt("HystorianHysteria_Data.txt"),0)
diff = 0
for val1, val2 in sorted_data:
    diff += abs(val1 - val2)
print(diff)
