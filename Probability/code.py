# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here
#task 1 - calculating joint probability

p_a = len(df[(df['fico']>700)])/len(df['fico'])
# print(p_a)
p_b = len(df[df['purpose']=='debt_consolidation'])/len(df['purpose'])
# print(p_b) 
df1 = df[df['purpose']=='debt_consolidation']
p_a_b = len(df1[df1['purpose']=='debt_consolidation'])*len(df1[df1['fico']>700])/len(df1[df1['fico']>700])
# print(p_a_b)
result = p_a_b == p_a
# print(f'This is result {result}')

#task 2  - calculating conditional probability
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df['paid.back.loan'])
# print(prob_lp)
prob_cs = len(df[df['credit.policy']=='Yes'])/len(df['credit.policy'])
# print(prob_cs)

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]

bayes = round((prob_pd_cs*prob_lp)/prob_cs,4)
print(bayes)

#step-3
df['purpose'].value_counts(normalize=True).plot(kind='bar')
plt.show()

df1 = df[df['paid.back.loan']=='No']
df1['purpose'].value_counts(normalize=True).plot(kind='bar')
plt.show()

#step-4
inst_median = df['installment'].median()

inst_mean = df['installment'].mean()

df['installment'].hist(normed=True,bins=50)
plt.show()


df['log.annual.inc'].hist(normed=True,bins=50)
plt.show()



