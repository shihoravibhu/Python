import matplotlib.pyplot as plt

x = range(1,11)
y = [10,15,13,18,20,22,19,25,30,28]

ax = plt.axes()

ax.plot(x,y,
        marker="*",
        linestyle=":",
        lw=2,
        c="red",
        alpha=0.7,
        label="India")

ax.legend(loc=2)

ax.annotate("Peak Score", xy=[9,30])

ax.set_xlim([0,12])
ax.set_ylim([0,35])
ax.set_xticks(range(0,13,2))
ax.set_yticks(range(0,36,5))

ax.grid(alpha=0.2)

plt.show()