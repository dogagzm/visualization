import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL


# Generate sample data
np.random.seed(613)
x = np.arange(50)
y = np.random.randint(0, 100, 50)

# Basic scatter plot
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y)
plt.show()

# Bar plot
fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(x, y)
plt.show()

# Line plot
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
plt.show()

# Histogram
fig, ax = plt.subplots(figsize=(5, 3))
ax.hist(y)
plt.show()

# Adding titles and labels
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.set_title('Total growth over time')
ax.set_ylabel('Total growth')
ax.set_xlabel('Years since start')
fig.tight_layout()
plt.show()

# Customizing titles and labels
font1 = {'family': 'sans-serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'monospace', 'color': 'green', 'size': 14}

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.set_title('Total growth over time', fontdict=font1)
ax.set_ylabel('Total growth', fontdict=font2)
ax.set_xlabel('Years since start', fontdict=font2)
fig.tight_layout()
plt.show()

# Moving labels
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.set_title('Total growth over time', fontdict=font1, loc='left')
ax.set_ylabel('Total growth', fontdict=font2)
ax.set_xlabel('Years since start', fontdict=font2)
fig.tight_layout()
plt.show()

# Customizing data points
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y, marker='*', color="indigo")
plt.show()

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*', color='indigo', linestyle='--', linewidth=2)
plt.show()

# Using hex color codes
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*', color='#7425b9', linestyle='--', linewidth=2)
plt.show()

# Further customization
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*', markersize=12, color='#7425b9', linestyle='--', linewidth=2, markeredgecolor='#fa9359', markerfacecolor='#fa9359')
plt.show()

# Adding grid lines
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.grid(axis='y', color="blue", linewidth=2, linestyle='-.')
plt.show()

#Scatter Plot: Different types of scatter plots are created to visualize relationships between data.
#Bar Plot: Bar plots are used to display data in categorical form.
#Line Plot: Line plots are used to show trends over time.
#Histogram: Histograms are used to visualize the distribution of data.
#Adding Titles and Labels: Titles and axis labels are added and customized for better readability.
#Customizing Data Points: Data points are customized with different markers, colors, and styles.
#Using Hex Color Codes: Hex color codes are used for precise color customization.
#Adding Grid Lines: Grid lines are added to improve data readability on the plot.
#These techniques enhance the ability to visualize and present data effectively.


import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests


np.random.seed(613)
x1 = np.arange(50)
y1 = np.random.randint(0, 75, 50)
x2 = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y2 = np.array([110, 180, 240, 99, 220])


fig, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(7, 3))
ax1.scatter(x1, y1)
ax2.bar(x2, y2)
plt.show()


fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'], ['ax2', 'ax3']], figsize=(7, 4))
for label, ax in someaxes.items():
    ax.text(0.5, 0.5, f'This is {label!r}', fontsize=14, ha='center', transform=ax.transAxes)

someaxes["ax1"].scatter(x1, y1)
someaxes["ax2"].bar(x2, y2)
someaxes["ax3"].plot(x1, y1)
plt.show()


fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'], ['ax2', 'ax3']], figsize=(7, 4), layout="constrained")
someaxes["ax1"].scatter(x1, y1)
someaxes["ax2"].bar(x2, y2)
someaxes["ax3"].plot(x1, y1)
someaxes["ax1"].set_xlabel('A Big Label', fontsize=18)
someaxes["ax2"].set_xlabel('Another Label', fontsize=18)
someaxes["ax3"].set_xlabel('Label 2: 2 Fast 2 Furious', fontsize=18)
plt.show()

#Creating Subplots: Different types of plots (scatter plot and bar plot) are displayed side by side using subplots.
#Subplots without Grid Arrangement: Subplots are created with a custom grid arrangement, displaying different types of plots (scatter, bar, and line) and adding text to each subplot for identification.
#Modifying Figure Layout: The layout of subplots is adjusted to improve spacing and alignment, and labels with larger font sizes are added to each subplot for better readability.
#These techniques enhance the ability to create and customize multiple plots within a single figure.


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests


np.random.seed(613)
x1 = np.arange(50)
y1 = np.random.randint(0, 75, 50)
x2 = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y2 = np.array([110, 180, 240, 99, 220])


fig, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(7, 3))
ax1.scatter(x1, y1)
ax2.bar(x2, y2)
plt.show()


fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'], ['ax2', 'ax3']], figsize=(7, 4))
for label, ax in someaxes.items():
    ax.text(0.5, 0.5, f'This is {label!r}', fontsize=14, ha='center', transform=ax.transAxes)

someaxes["ax1"].scatter(x1, y1)
someaxes["ax2"].bar(x2, y2)
someaxes["ax3"].plot(x1, y1)
plt.show()


fig, someaxes = plt.subplot_mosaic([['ax1', 'ax3'], ['ax2', 'ax3']], figsize=(7, 4), layout="constrained")
someaxes["ax1"].scatter(x1, y1)
someaxes["ax2"].bar(x2, y2)
someaxes["ax3"].plot(x1, y1)
someaxes["ax1"].set_xlabel('A Big Label', fontsize=18)
someaxes["ax2"].set_xlabel('Another Label', fontsize=18)
someaxes["ax3"].set_xlabel('Label 2: 2 Fast 2 Furious', fontsize=18)
plt.show()

#Creating Basic Subplots: Two subplots are created side by side, with a scatter plot in one and a bar plot in the other.
#Custom Grid Arrangement: Subplots are arranged in a custom grid layout, showing different types of plots (scatter, bar, and line) and adding descriptive text to each subplot.
#Adjusting Figure Layout: The layout of subplots is refined with the "constrained" setting to improve spacing and alignment, and large, descriptive labels are added to each subplot for clarity.
#These methods help in effectively organizing and presenting multiple plots within a single figure.


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests
import seaborn as sns
import plotly.express as px


np.random.seed(613)
x = np.arange(50)
y = np.random.randint(0, 100, 50)
x1 = np.arange(50)
y1 = np.random.randint(0, 75, 50)
x2 = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y2 = np.array([110, 180, 240, 99, 220])
data = pd.DataFrame({'x': x, 'y': y})


fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y)
plt.show()


fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(x, y)
plt.show()


fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
plt.show()

fig, ax = plt.subplots(figsize=(5, 3))
ax.hist(y)
plt.show()


fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.set_title('Total growth over time')
ax.set_ylabel('Total growth')
ax.set_xlabel('Years since start')
fig.tight_layout()
plt.show()

font1 = {'family': 'sans-serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'monospace', 'color': 'green', 'size': 14}

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.set_title('Total growth over time', fontdict=font1)
ax.set_ylabel('Total growth', fontdict=font2)
ax.set_xlabel('Years since start', fontdict=font2)
fig.tight_layout()
plt.show()


fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.set_title('Total growth over time',
             

#Basic Plots with Matplotlib:

#Scatter Plot: Displays the relationship between x and y values.
#Bar Plot: Shows the distribution of y values with respect to x.
#Line Plot: Illustrates the trend in y values over x.
#Histogram: Visualizes the distribution of y values.
#Enhancing Plots:

#Adding Titles and Labels: Titles and axis labels are added to improve plot readability and context.
#Custom Fonts and Colors: Customized font properties for titles and labels to make them more visually appealing.
#Data Handling with Pandas:

#Creating a DataFrame: Demonstrates how to structure data using a Pandas DataFrame for plotting.
#These techniques provide a comprehensive approach to creating, customizing, and presenting various types of plots using Matplotlib, along with basic data handling with Pandas.