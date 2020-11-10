# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
property_and_loan = data.groupby(['Property_Area','Loan_Status'])['Loan_Status'].count().unstack()

#Plotting bar plot

property_and_loan.plot(kind='bar',stacked=True,figsize=(10,7))
plt.title('Property Vs Loan Status')
plt.xlabel('Property Area',fontsize=14,color='orange')
plt.ylabel('Loan Status',fontsize=14,color='green')
plt.xticks(rotation=45)
plt.show()




# Step 2
#Plotting an unstacked bar plot

education_and_loan = data.groupby(['Education','Loan_Status'])['Loan_Status'].count().unstack()


#Changing the x-axis label

education_and_loan.plot(kind='bar',stacked=True,figsize=(10,7))
plt.title('Education Vs Loan Status')
plt.xlabel('Education Status',fontsize=14,color='orange')
plt.ylabel('Loan Status',fontsize=14,color='green')
plt.xticks(rotation=45)
plt.show()
#Changing the y-axis label

graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
#Rotating the ticks of X-axis
graduate['LoanAmount'].plot(kind='density',label='Graduate',figsize=(10,6))
plt.xlabel('Loan Amount in Lacs',fontsize=15)
plt.title('Loan Amount Density Plot For Graduates',fontsize=15,color='Blue')
plt.show()


not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate',figsize=(10,6))
plt.xlabel('Loan Amount in Lacs',fontsize=15)
plt.title('Loan Amount Density Plot For Not Graduates',fontsize=15,color='Blue')
plt.show()

# Step 3
#Plotting a stacked bar plot




#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column


#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'


#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots


#Plotting scatter plot


#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



data['TotalIncome'] = data['ApplicantIncome']+data['CoapplicantIncome']
#Setting the subplot axis title
fig , (ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize=(10,20))
data.plot.scatter(x='ApplicantIncome',y='LoanAmount',ax=ax_1)
ax_1.set_title('Applicant Income Vs Loan amount')

data.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
ax_2.set_title('Coapplicant Income Vs Loan amount')


data.plot.scatter(x='TotalIncome',y='LoanAmount',ax=ax_3)
ax_3.set_title('Total Income Vs Loan amount')

plt.show()


