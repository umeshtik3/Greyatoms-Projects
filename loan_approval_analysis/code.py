# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)

#separating categorial variables from data
categorical_var = bank_data.select_dtypes(exclude='number')

#separting numerical variable from data
numerical_var = bank_data.select_dtypes(include='number')
numerical_var
print(categorical_var.shape,numerical_var.shape)

banks = bank_data.drop(columns='Loan_ID')

bank_mode = banks.mode()


for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)

avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean').reset_index()

loan_stauts_se = banks[(banks['Self_Employed']== 'Yes' ) & (banks['Loan_Status']=='Y')]

loan_stauts_nse = banks[(banks['Self_Employed']== 'No' ) & (banks['Loan_Status']=='Y')]

percentage_se = round((len(loan_stauts_se)/614)*100,2)
percentage_nse = round((len(loan_stauts_nse)/614)*100,2)
print(percentage_nse,percentage_se)

loan_term = banks['Loan_Amount_Term'].apply(lambda x : x /12 )
big_loan_term = []
for i in loan_term:
    if i >= 25 :
        big_loan_term.append(i)
print(len(big_loan_term))


mean_values = banks.groupby(['Loan_Status'])['ApplicantIncome','Credit_History'].mean()

print(mean_values)
#Code starts here




