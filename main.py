import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [140, 10, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.savefig('bars.png', bbox_inches='tight')

cat = ["bored", "happy", "happy", "happy", "happy", "bored"]
dog = ["bored", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

fig, ax = plt.subplots()
ax.plot(activity, dog, label="dog")
ax.plot(activity, cat, label="cat")
ax.legend()

plt.savefig('lines.png', bbox_inches='tight')


y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 

plt.savefig('pie.png', bbox_inches='tight')


x = np.array([1, 2, 3, 4])  # X-axis points 
y = x*2  # Y-axis points 
  
plt.plot(x, y)  # Plot the chart 
plt.savefig('line.png',bbox_inches='tight')
