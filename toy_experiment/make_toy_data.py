from random import random

N_FILES = 1000
HEADER = ["x", "y"]
N_ROWS = 100

for i in range(N_FILES):
    with open(f"./toy_dataset/input_{i}.csv", "w", newline='\n') as f:
        f.write(",".join(HEADER) + "\n")
        for _ in range(N_ROWS):
            f.write("{x},{y}\n".format(x=random(), y=random()))
