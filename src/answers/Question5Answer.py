import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import os
from os import path

# Get our data
def extract_crime_data_from_alaska():
    with open(path.join(os.path.realpath(__file__), "..", "alaska.csv"), "r") as file:
        data = file.readlines()

        # Remove the headers from the csv file
        data = data[2:]

        for i in range(len(data)):
            # Split the columns of the csv
            splits = data[i].split(',')

            # Replace the csv string entry with the individual elements they represent
            data[i] = []

            for j in range(len(splits)):
                data[i].append(splits[j])

        return data
        
alaska = extract_crime_data_from_alaska()

alaska_matrix = np.array(alaska)

years = alaska_matrix[:,2]
total_crimes = alaska_matrix[:,4]
print(total_crimes)
print(years)

print(len(total_crimes))
print(len(years))

# Create a plot
fig, ax = plt.subplots()
ax.plot(years, total_crimes)

# Configure the graph
ax.set(xlabel='Years', ylabel='Total Crimes',
    title='Question 4')
ax.set_ylim(ymin=0)
ax.grid()

# Show the graph
fig.savefig("ok.png")
plt.show()