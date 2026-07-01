import matplotlib.pyplot as plt

Categories = ["Rent", "Food", "Education", "Transport", "Entertainment", "Savings"]
Amount = [15000, 8000, 6000, 3000, 2000, 5000]

plt.pie(Amount , labels=Categories , autopct = "%1.2f%%" , colors = ["lightblue","g","hotpink","m","b","y"],explode=[0,0,0,0,0,0.1])
plt.title("Your Title")
# plt.show()