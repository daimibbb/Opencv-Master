import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

plt.rcdefaults()
fig, ax = plt.subplots()

people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_ind = np.arange(len(people))
performance = 3 + 10 * np.random.rand((len(people)))
error = np.random.rand(len(people))

ax.barh(y_ind, performance, xerr=error, align='center',color='green', ecolor='black')
ax.set_yticks(y_ind)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()