import seaborn as sns
import matplotlib.pyplot as plt

# Load the planets dataset
planets = sns.load_dataset('planets')

# Relational plots
plt.figure(figsize=(12, 6))
sns.scatterplot(x='distance', y='mass', hue='method', data=planets)
plt.title('Scatter Plot of Distance vs Mass')
plt.xlabel('Distance')
plt.ylabel('Mass')
plt.legend(title='Detection Method')
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='distance', hue='method', data=planets)
plt.title('Line Plot of Year vs Distance')
plt.xlabel('Year')
plt.ylabel('Distance')
plt.legend(title='Detection Method')
plt.show()

# Distributional plots
plt.figure(figsize=(12, 6))
sns.histplot(planets['mass'], kde=True)
plt.title('Histogram of Planet Mass')
plt.xlabel('Mass')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='method', y='mass', data=planets)
plt.title('Box Plot of Mass by Detection Method')
plt.xlabel('Detection Method')
plt.ylabel('Mass')
plt.xticks(rotation=90)
plt.show()

# Categorical plots
plt.figure(figsize=(12, 6))
sns.barplot(x='method', y='distance', data=planets)
plt.title('Bar Plot of Distance by Detection Method')
plt.xlabel('Detection Method')
plt.ylabel('Distance')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='method', data=planets)
plt.title('Count Plot of Detection Methods')
plt.xlabel('Detection Method')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

# Conclusions
conclusions = """
Conclusions:
1. The scatter plot of Distance vs Mass shows that there is no clear relationship between the distance of a planet and its mass. However, it does show the variety of detection methods used.
2. The line plot of Year vs Distance illustrates how the distance of discovered planets has changed over time, with different methods being more prominent in different years.
3. The histogram of Planet Mass shows the distribution of planet masses, indicating that most planets have a mass less than 20 units.
4. The box plot of Mass by Detection Method shows the spread and outliers of planet masses for each detection method, highlighting that some methods tend to find heavier planets.
5. The bar plot of Distance by Detection Method shows the average distance of planets discovered by each method, indicating that some methods are better at finding distant planets.
6. The count plot of Detection Methods shows the frequency of each detection method, illustrating which methods are most commonly used.

The scatter plot of Distance vs Mass and the line plot of Year vs Distance best demonstrate notable aspects of the data. The scatter plot highlights the diversity of detection methods and the lack of a clear relationship between distance and mass, while the line plot shows the evolution of planet discovery over time.
"""

print(conclusions)
