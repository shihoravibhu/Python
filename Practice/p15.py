import matplotlib.pyplot as plt

labels = ['Electronics', 'Clothing', 'Home Appliances', 'Books', 'Others']
sizes = [35, 25, 20, 10, 10]
colors = ['blue', 'green', 'orange', 'purple', 'red']

plt.pie(sizes, labels=labels, autopct='%1.0f%%', colors=colors)

plt.title("Sales Distribution")

plt.savefig("chart.png")
plt.savefig("chart.pdf")

plt.show()