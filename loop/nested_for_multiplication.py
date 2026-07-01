import numpy as np
numb = np.array([1, 2, 3, 4, 5])
for i in range(1, 13):            
    print(numb * i)

for i in range(1, 3):
    for j in range(1, 6):
        print(i * j, end ="\t")

    print()

for i in range(1, 6):
    print(i)