# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here
data['Gender'].replace(to_replace='-',value= 'Agender',inplace=True)

gender = data['Gender'].value_counts()
#plot a graph for gender
gender.plot(kind='bar',figsize=(10,6))
plt.xlabel('Gender')
plt.ylabel('count')
plt.title('Gender Distribution')
plt.show()

data['Alignment'].value_counts().plot(kind='bar')

new_df = data[['Intelligence', 'Strength', 'Combat']]

new_df.corr(method='pearson')

q1 = data['Total'].quantile(0.99)

super_best_names = data[data['Total']>q1]['Name'].values



