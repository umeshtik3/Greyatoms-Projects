# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((new_record,data))


age = census[:,0]
min_age = np.min(age)
max_age = np.max(age)
age_mean = np.std(age)
age_std = np.mean(age)
print(min_age,max_age,age_mean,age_std)


race = census[:,2]
race_0 = [i for i in race if i==0 ]
race_1 = [i for i in race if i==1 ]
race_2 = [i for i in race if i==2 ]
race_3 = [i for i in race if i==3 ]
race_4 = [i for i in race if i==4 ]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
length = [len_0,len_1,len_2,len_3,len_4]
minority_race = length.index(len_3)

senior_citizens = census[census[:,0]>60]
working_hours_sum = np.sum(senior_citizens[:,6])
senior_citizen_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizen_len

high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = round(np.mean(high[:,7]),2)
avg_pay_low = round(np.mean(low[:,7]),2)




