# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank=pd.read_csv(path) 
# code starts here
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include='number')
print(numerical_var)
# code ends here


# --------------
# code starts here
bank.drop(['Loan_ID'],inplace=True,axis=1)
banks=bank
print(banks.isnull().sum())
bank_mode=banks.mode()
cols=banks.columns
print(cols)
for i in cols:
    banks[i].fillna(i,inplace=True)
#print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
import pandas as pd
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount')
print(avg_loan_amount)






# code ends here



# --------------
# code starts here
loan_approved_se=banks[(banks['Self_Employed']=='Yes')&(banks['Loan_Status']=='Y')]['Gender'].count()
print(loan_approved_se)
loan_approved_nse=banks[(banks['Self_Employed']=='No')&(banks['Loan_Status']=='Y')]['Gender'].count()
print(loan_approved_nse)
Loan_Status=614
percentage_se=((loan_approved_se)/(Loan_Status))*100
print(percentage_se)
percentage_nse=((loan_approved_nse)/(Loan_Status))*100
print(percentage_nse)


# code ends here


# --------------
# code starts here

def Mon_Yrs(x):
    return x/12
loan_term=banks['Loan_Amount_Term'].apply(lambda x: Mon_Yrs(x))
banks['Loan_Amount_Term']=loan_term
print(banks['Loan_Amount_Term'])
big_loan_term=banks[banks['Loan_Amount_Term']>=25]['Loan_Amount_Term'].count()
print(big_loan_term)



# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby(['Loan_Status'])
#print(loan_groupby.groups)
loan_groupby=loan_groupby[['ApplicantIncome','Credit_History']]
#print(loan_groupby.groups)
mean_values=loan_groupby.mean()
print(mean_values)


# code ends here


