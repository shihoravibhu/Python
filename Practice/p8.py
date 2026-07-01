import matplotlib.pyplot as plt
import random

marks = [random.randint(40,100) for _ in range(300)]

# plt.hist(marks)
# plt.hist(marks, bins=5)
# plt.hist(marks,
#          bins=[40,50,60,70,80,90,100])
# plt.hist(
#     marks,
#     bins=5,
#     edgecolor='r',
#     color='gray'
# )
t1 = plt.hist(marks)

plt.bar_label(t1[2])

plt.show()