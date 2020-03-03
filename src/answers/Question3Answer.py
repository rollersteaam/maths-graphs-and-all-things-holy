# Question 3: This Is What You Came For
# Plot the attendance matrix as a graph.

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Get our data
x = np.array([20, 60, 20, 90, 95])
y = np.array([85, 40, 90, 80, 75])

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Configure the graph
ax.set(xlabel='Attendance (%)', ylabel='Exam Performance (%)',
    title='Question 1 :)')
ax.grid()
ax.set_ylim(ymin=0, ymax=100)
ax.set_xlim(xmin=0, xmax=100)

# Show the graph
fig.savefig("ok.png")
plt.show()