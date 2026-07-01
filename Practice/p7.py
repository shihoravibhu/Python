import matplotlib.pyplot as plt

subjects = ['Python','DBMS','SE','PS','PC']
students = [120,145,70,100,40]

colors = ['pink','r','g','y','m']

plt.pie(students, labels=subjects, colors=colors, shadow=True)

plt.show()