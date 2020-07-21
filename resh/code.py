# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file

data = np.genfromtxt(path, delimiter=",", skip_header=1)
census=np.concatenate((data, new_record),axis = 0)
print(data.shape)
print(census.shape)
age=census[:,0]
max_age=age.max()
print(max_age)
min_age=age.min()
print(min_age)
min_age=age.min()
print("Min Age= ",min_age)
age_std=age.std()
print(age_std)
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

print('race_0:',len_0)
print('race_1:',len_1)
print('race_2:',len_2)
print('race_3:',len_3)
print('race_4:',len_4)

race_list=[len_0,len_1,len_2,len_3,len_4]
minority_race=race_list.index(min(race_list))
print(minority_race)
senior_citizens=census[census[:,0]>60]
working_hrs_sum=senior_citizens.sum(axis=0)[6]
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hrs_sum/senior_citizens
print(avg_working_hours)
high=census[census[:,1]>10]
avg_pay_high=high[:,7].mean()
print(avg_pay_high)
low=census[census[:,1]<=10]
avg_pay_low=low[:,7].mean()
print(avg_pay_low)


