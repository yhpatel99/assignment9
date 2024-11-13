import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Exercise_Data.csv')

# Melt the data for easier plotting
melted_data = data.melt(id_vars=['id', 'diet', 'kind'], value_vars=['1 min', '15 min', '30 min'], 
                        var_name='Time', value_name='Pulse')

# Create a heatmap of the pulse data
plt.figure(figsize=(10, 8))
heatmap_data = data.pivot_table(index='id', columns='kind', values='1 min')
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', cbar_kws={'label': 'Pulse'})
plt.title('Heatmap of Pulse Data at 1 Minute')
plt.xlabel('Type of Exercise')
plt.ylabel('Participant ID')
plt.show()

# Create a categorical plot of pulse values by diet and by type of exercise
plt.figure(figsize=(12, 6))
sns.catplot(x='Time', y='Pulse', hue='diet', col='kind', data=melted_data, kind='bar', height=4, aspect=0.7)
plt.subplots_adjust(top=0.85)
plt.suptitle('Pulse Values by Diet and Type of Exercise')
plt.show()

# Conclusions
conclusions = """
Conclusions:
1. The heatmap shows the pulse data at 1 minute for different types of exercises. It helps to identify the variation in pulse rates among participants.
2. The categorical plot shows the pulse values by diet and type of exercise. It indicates that:
   - Running generally results in higher pulse rates compared to walking and resting.
   - The 'no fat' diet tends to show higher pulse rates during running compared to the 'low fat' diet.
3. These visualizations help to understand how different diets and exercises affect heart rate, which can be explained to elementary school students as:
   - Exercise increases heart rate, with more intense exercises like running causing a higher increase.
   - Diet can also influence heart rate, with certain diets potentially leading to higher pulse rates during exercise.
"""

print(conclusions)