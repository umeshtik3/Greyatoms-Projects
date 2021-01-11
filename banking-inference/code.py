# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here
data_sample = data.sample(n=sample_size,random_state = 0)
print(data_sample.shape)
#population mean
true_mean = data['installment'].mean()
#population standard deviation
true_std = data_sample['installment'].std()
#sample mean
sample_mean = data_sample['installment'].mean()
#sample standard deviation
sample_std = data_sample['installment'].std()
#margin of error
margin_of_error = z_critical*(true_std/(np.sqrt(sample_size)))
print('Margin of error is',margin_of_error)
print('=='*30)
#confidence interval
confidence_interval = [round(sample_mean-margin_of_error,2),round(sample_mean+margin_of_error,2)]

print('Confidence Interval is ',confidence_interval)
print('=='*30)
print('True mean is',true_mean)
print('=='*30)

#Central Limit theorem for installment column
print('Central Limit Theorem for installment column')

#creating array of three sample sizes
## sample from population with different number of sampling
# a list of sample mean
meansample = []
# number of sample
numofsample = 1000
# sample size
samplesize = [20,50,100]
# for each number of sampling (1000 to 50000)
array_1 = []


for j in range(1,1000):
    for i in samplesize:
        array_1.append(data['installment'].sample(n=100,replace= True).mean())
    
#print(array)
plt.hist(array_1, bins=100)

plt.xlabel('installment')
plt.ylabel('frequency')
plt.title('Histogram of Installment frequency')
plt.axvline(x=np.mean(array_1),color='r')

print('=='*30)
print(' Performing the Z-test on int.rate')
data['int.rate'] = data['int.rate'].map(lambda x : x.split('%')[0])
data['int.rate'] = data['int.rate'].astype(float)
df_ = data[data['purpose']=='small_business']
value_ = data['int.rate'].mean()

z_statistic_1 ,p_value_1 = ztest(df_['int.rate'],value=value_,alternative='larger')
print('z-test is ',z_statistic_1)
print('=='*30)
print('p-value is',p_value_1)

print('=='*30)
print('Performing the two-sided the z-test on installments')
installment_paid_mean = data[data['paid.back.loan']=='Yes']['installment']
installment_notpaid_mean = data[data['paid.back.loan']=='No']['installment']

z_statistic_2 ,p_value_2 = ztest(x2 = installment_paid_mean,x1=installment_notpaid_mean,alternative='two-sided')
print('z-test is ',z_statistic_2)
print('=='*30)
print('p-value is',p_value_2)

print('=='*30)
print('Performing chi-test on purpose and loan default' )
yes=data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no=data[data['paid.back.loan']=='No']['purpose'].value_counts()


#Concating yes and no into a single dataframe
observed=pd.concat([yes.transpose(),no.transpose()], 1,keys=['Yes','No'])

print(observed)

chi2, p, dof, ex = chi2_contingency(observed)



