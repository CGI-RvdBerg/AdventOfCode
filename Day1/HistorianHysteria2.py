import numpy as np

data = np.loadtxt("HystorianHysteria_Data.txt").T
similarity_score = 0
for val1 in data[0]:
    count = np.sum(data[1] == val1)
    similarity_score += val1 * count
print(similarity_score)