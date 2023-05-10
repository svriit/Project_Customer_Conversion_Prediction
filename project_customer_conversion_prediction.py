# -*- coding: utf-8 -*-
"""Project_Customer_Conversion_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dGQpotLzvbWU3BBEn7mnca9OkQlRTgas

<a href="https://colab.research.google.com/github/pdivya-mca/Customer-Conversion-Prediction/blob/main/Project_Customer_Conversion_Prediction.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#To ignore warnings
import warnings
warnings.filterwarnings("ignore")

"""# **Loading Dataset**"""

df=pd.read_csv("train.csv")

"""# **Analysis of Data**"""

# Checking size of dataset
print("Data set size : ", df.shape)

"""From the above result no of rows are 45211 and no of columns are 11"""

#Fetching top 5 row in dataset
df.head()

#Fetching Bottom 5 rows
df.tail()

#finding the column names
df.columns

#Basic statistical analysis of dataset
df.describe()

"""From statistical result we can understatnd the basic statistical report of min, max, percentile, mean and standard deviation"""

#checking for the data is balanced or not
df['y'].value_counts()

"""From the above result we can clearly understand that the dataset is imbalanced. Lets find the percentage."""

#Finding the percentage of the data
print('Percentage for "no": ',((39916) / (39916+5289)) * 100 )
print('Percentage for "yes": ',((5289) / (39916+5289)) * 100 )

"""from the above result we can clearly understand that the percentage for no is very high so the Majority class "no" with 88.29% and Minority class "yes" with 11.7%.

# **Data Preprocessing**
# **Data Cleaning**

### **Missing Values**
"""

#checking for null values
df.isnull().sum()

"""### **Finding Duplicate Values**"""

#checking for no of duplicate values
df.duplicated().sum()

"""From the above result we can find 6 duplicate datas. So will drop the duplicates."""

#droping duplicates
df = df.drop_duplicates()

#after droping agin check for no of duplicates
df.duplicated().sum()

"""Duplicates are removed from dataset.

### **Checking Data Type**
"""

df.dtypes

"""There is no need to change any datatype of the columns

### **Unique Values of Categorical Column**
"""

print("Unique values of Job \n")
print(df['job'].unique())

print("Unique values of Marital Status \n")
print(df['marital'].unique())

print("Unique values of Educationsl Qualification \n")
print(df['education_qual'].unique())

print("Unique values of Call Type \n")
print(df['call_type'].unique())

print("Unique values of Month \n")
print(df['mon'].unique())

print("Unique values of Previous Outcome \n")
print(df['prev_outcome'].unique())

print("Unique values of Target Variable 'y' \n")
print(df['y'].unique())

"""From all the above results all values are unique which means there is no incorrect or wrong data that is spelling mistake, upper case and lower case mismatch of each values.

### **Exploring the Dataset and replace the unknown values**

**Converting categorical Target column into numerical column.**
"""

df['target'] = df["y"].map({"yes":1 , "no": 0})

df.head()

"""**Age**"""

#no of counts for particular age 
df.age.value_counts()

#checking for the percentage of how many people get insured? compared with Target vs Age
df.groupby('age')['target'].mean()

"""**Job**"""

#no of counts for particular job
df.job.value_counts()

#checking for the percentage of how many people get insured? compared with Target vs Job
df.groupby('job')['target'].mean()

# droping the column unknown 
#outof 45211 rows, deletion of 288 rows will not get more impact on dataset so planning to delete

#replacing unknown value as null
df['job'] =df['job'].replace('unknown',np.nan)

#counting the no of null value in jab column
df.job.isnull().sum()

#removing null values from job column
df=df.dropna(subset=['job'])

#after removing null values checking for the summ of null vaues
df.job.isnull().sum()

"""**Marital Status**"""

#no of counts for marital status
df.marital.value_counts()

#checking for the percentage of how many people get insured? compared with Target vs Marital Status
df.groupby('marital')['target'].mean()

"""**Educational Qualification**"""

#no of counts for Educational qualification
df.education_qual.value_counts()

#checking for the percentage of how many people get insured? compared with Target vs Educational Qualification
df.groupby('education_qual')['target'].mean()

#Finding the percentage of unknown value
print('Percentage for "Unknown": ',((1730) / (23202+13301+6851+1730)) * 100 )

"""Unknown percentage is 3.8% so if we delete also it will note affect the dataset"""

#replacing unknown value as null
df['education_qual'] =df['education_qual'].replace('unknown',np.nan)

#checking for null values
df.education_qual.isnull().sum()

#droping the null values
df = df. dropna(subset=['education_qual'])

#checking for null value after deleting
df.education_qual.isnull().sum()

"""**Call Type**"""

#no of counts for Call type
df.call_type.value_counts()

#checking for the percentage of how many people get insured? compared with Target vs Call Type
df.groupby('call_type')['target'].mean()

#Finding the percentage of unknown value
print('Percentage for "Unknown": ',((12283) / (29285+13020+12283)) * 100 )

"""Unknown call type percentage is 22.50% so we will keep as it is.

**Day**
"""

#no of counts for Day
df.day.value_counts()

#checking for the percentage of how many people get insured? compared with Target vs Day
df.groupby('day')['target'].mean()

"""**Month**"""

#no of counts for month
df.mon.value_counts()

#checking for the percentage of how many people get insured? compared with Target vs Month
df.groupby('mon')['target'].mean()

"""**Duration**"""

#no of counts for duration
df.dur.value_counts()

#checking for the percentage of how many people get insured? compared with Target vs Duration
df.groupby('dur')['target'].mean()

"""**Number of Calls**"""

#no of counts for number of calls
df.num_calls.value_counts()

#checking for the percentage of how many people get insured? compared with Target vs Numer of Calls
df.groupby('num_calls')['target'].mean()

"""**Previous Outcome**"""

#no of counts for previous outcome
df.prev_outcome.value_counts()

#checking for the percentage of how many people get insured? compared with Target vs Previous outcome
df.groupby('prev_outcome')['target'].mean()

#Finding the percentage of unknown value
print('Percentage for "Unknown": ',((35280) / (35280+4709+1774+1424)) * 100 )

"""It is around 81% values are unknown. So will keep unknown value as it is.

**Target Variable Y**
"""

#no of counts of target variable y
df.y.value_counts()

df.info()

"""### **Outlier Deduction and Correction**
**Outlier Detection**
1.   Z-Score
2.   IQR
3.   Plotting
      Box Plot

**Outlier Correction**
1.   Deletion
2.   Clip/Strip


"""

df.info()

"""## **Age**

**Box Plot**
"""

#Outlier Detuction using Box Plot for Age Column
sns.set(style="whitegrid")
sns.boxplot(x=df['age'], color='Chartreuse')

"""From outlier we can see that there are many dots are displayed outside whisker.

**IQR**
"""

#detecting Outlier for Age column
q1,q3=np.percentile(df["age"],[25,75])
IQR=q3-q1
upper=q3+1.5*IQR
lower=q1-1.5*IQR
print("Upper age bound:",upper,"Lower age bound :", lower)

"""**Removing outlier for Age**"""

#removing outlier for age column
# Clip/ Strip is used to detuct value to lower & upper threshold.
df.age = df.age.clip(10.5,70.5)

df.age.describe()

"""**Checking- After outlier removal**"""

sns.set(style="whitegrid")
sns.boxplot(x=df['age'], color='Chartreuse')

"""## **Day**

**Box Plot**
"""

#Outlier Detuction using Box Plot for day Column
sns.set(style="whitegrid")
sns.boxplot(x=df['day'], color='Chartreuse')

"""**IQR**"""

#detecting Outlier for Age column
q1,q3=np.percentile(df["day"],[25,75])
IQR=q3-q1
upper=q3+1.5*IQR
lower=q1-1.5*IQR
print("Upper bound:",upper,"Lower bound :", lower)

df.day.describe()

"""From Box plot itself we can tell there is no outlier, even though checked with IQR approach. min and max values are in between lower and upper bound.

## **Duration**

**Box Plot**
"""

#Outlier Detuction using Box Plot for duration Column
sns.set(style="whitegrid")
sns.boxplot(df['dur'], color='Chartreuse')

"""**IQR**"""

q1,q3=np.percentile(df["dur"],[25,75])
IQR=q3-q1
upper=q3+1.5*IQR
lower=q1-1.5*IQR
print("Upper bound:",upper,"Lower bound :", lower)

"""**Removing Outlier for duration column**"""

df.dur = df.dur.clip(-219.5,640.5)

df.dur.describe()

"""**Checking after outlier removal**"""

sns.set(style="whitegrid")
sns.boxplot(df['dur'], color='Chartreuse')

"""## **No of Calls**

**Box Plot**
"""

sns.set(style="whitegrid")
sns.boxplot(df['num_calls'], color='Chartreuse')

"""**IQR**"""

q1,q3=np.percentile(df["num_calls"],[25,75])
IQR=q3-q1
upper=q3+1.5*IQR
lower=q1-1.5*IQR
print("Upper bound:",upper,"Lower bound :", lower)

#removing outlier for num_calls column
# Clip/ Strip is used to detuct value to lower & upper threshold.
df.num_calls = df.num_calls.clip(-2,6.0)

df.num_calls.describe()

"""**Checking after outlier removal**"""

sns.set(style="whitegrid")
sns.boxplot(df['num_calls'], color='Chartreuse')

"""# **Features vs Target**

# **Encoding**
In this project i am going to use decision tree so we muct do label encoding.
"""

df.columns

"""### **Job**"""

#Encoding for job column (Label Encoding)
df['job']=df['job'].map({'blue-collar':1,'entrepreneur':2,'services':3,'housemaid':4,'technician':5,'self-employed':6,'admin.':7,'management':8, 'unemployed':9, 'retired': 10, 'student' : 11})   
df.head(3)

"""### **Marital Status**"""

#Encoding for Marital status (Label Encoding)
df['marital'] =df['marital'].map({'married': 1, 'divorced': 2, 'single' : 3})
df.head(3)

"""### **Educational Qualification**"""

#encoding for educational qualification (Label Encoding)
df['education_qual'] = df['education_qual'].map({'primary': 1, 'secondary': 2, 'tertiary' :3})
df.head(3)

"""### **Month**"""

# Encoding for month column (Label Encoding)
df['mon']=df['mon'].map({'may': 1, 'jul' : 2, 'jan': 3, 'nov': 4, 'jun' : 5, 'aug' : 6, 'feb' : 7, 'apr' : 8, 'oct' : 9, 'dec' : 10 , 'sep': 11, 'mar': 12})
df.head(3)

"""### **Call Type**"""

# Encoding for call type column (Label Encoding)
df['call_type'] = df['call_type'].map({'unknown': 1, 'telephone' : 2, 'cellular' : 3})
df.head(3)

"""### **Previous Outcome**"""

# Encoding for previous outcome column (Label Encoding)
df['prev_outcome']=df['prev_outcome'].map({'unknown' : 1, 'failure' : 2, 'other' : 3, 'success': 4})
df.head(3)

"""# **Feature and Target Selection**"""

df.columns

# X --> Feature y-- > Target

x = df[['age', 'job', 'marital', 'education_qual', 'call_type', 'day', 'mon', 'dur', 'num_calls', 'prev_outcome']].values
y=df['target'].values

"""# **Spliting**"""

# splitting the data as train and test

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state = 3 )

"""# **Balancing**"""

#Balancing the data
from imblearn.combine import SMOTEENN 
smt = SMOTEENN(sampling_strategy='all') 
x_train_smt, y_train_smt = smt.fit_resample(x_train, y_train)

print(len(x_train_smt))
print(len(y_train_smt))

"""# **Scaling**"""

#scaling the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train_smt)
x_test_scaled = scaler.transform(x_test)

"""# **Modelling**

## **Logistic Regression**
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

lr = LogisticRegression()

lr.fit(x_train_scaled,y_train_smt)
lr.score(x_test_scaled,y_test)

y_pred=lr.predict_proba(x_test_scaled)
y_pred

log_reg_auroc = roc_auc_score(y_test,y_pred[:,1])
print("AUROC score for logistic regression  :  ",round(log_reg_auroc,2))

"""## **K-Nearest Neighbour (KNN)**"""

from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import cross_val_score 
for i in [1,2,3,4,5,6,7,8,9,10,20,30,40,50]: 
  knn= KNeighborsClassifier(i)
  knn.fit(x_train_scaled, y_train_smt) 
  print("K value :", i, "Train Score : ", knn.score(x_train_scaled,y_train_smt), "Cross Value Accuracy :" , np.mean(cross_val_score(knn, x_test_scaled, y_test, cv=10)))

"""**k=10 is a good cross validation accuracy of 0.895**"""

knn= KNeighborsClassifier(i)
knn.fit(x_train_scaled, y_train_smt)
print("KNN Score: ",knn.score(x_test_scaled,y_test)) 
print( "AUROC on the sampled dataset : ",roc_auc_score( y_test, knn.predict_proba(x_test)[:, 1]))

"""## **Decision Tree**"""

from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import roc_auc_score

from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import roc_auc_score 
dt = DecisionTreeClassifier() 
dt.fit(x_train_smt,y_train_smt) 
print("Decision Tree Score : ", dt.score(x_train_smt,y_train_smt)) 
print( "AUROC on the sampled dataset : ",roc_auc_score( y_test, dt.predict_proba(x_test)[:, 1]))

from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import cross_val_score #this will help me to do cross- validation
import numpy as np

for depth in [1,2,3,4,5,6,7,8,9,10,20]:
  dt = DecisionTreeClassifier(max_depth=depth) # will tell the DT to not grow past the given threhsold
  # Fit dt to the training set
  dt.fit(x_train_smt, y_train_smt) # the model is trained
  trainAccuracy = accuracy_score(y_train_smt, dt.predict(x_train_smt)) # this is useless information - i am showing to prove a point
  dt = DecisionTreeClassifier(max_depth=depth) # a fresh model which is not trained yet
  valAccuracy = cross_val_score(dt, x_test_scaled, y_test, cv=10) # syntax : cross_val_Score(freshModel,fts, target, cv= 10/5)
  print("Depth  : ", depth, " Training Accuracy : ", trainAccuracy, " Cross val score : " ,np.mean(valAccuracy))

"""**k= 5 is the good cross validation score of 0.896**"""

dt = DecisionTreeClassifier(max_depth=5) 
dt.fit(x_train_smt,y_train_smt) 
print("Decision Tree Score : ", dt.score(x_train_smt,y_train_smt)) 
print( "AUROC on the sampled dataset : ",roc_auc_score( y_test, dt.predict_proba(x_test)[:, 1]))

"""## **XG Boost**"""

import xgboost as xgb
from sklearn.model_selection import cross_val_score 
import numpy as np 
for lr in [0.01,0.02,0.03,0.04,0.05,0.1,0.11,0.12,0.13,0.14,0.15,0.2,0.5,0.7,1]: 
  model = xgb.XGBClassifier(learning_rate = lr, n_estimators=100, verbosity = 0) # initialise the model 
  model.fit(x_train_smt,y_train_smt) #train the model 
  print("Learning rate : ", lr," Train score : ", model.score(x_train_smt,y_train_smt)," Cross-Val score : ", np.mean(cross_val_score(model, x_test, y_test, cv=10)))

"""**Learning Rate 0.2 is getting the best cross validation score of 0.899**

## **Random Forest**
"""

from sklearn.ensemble import RandomForestClassifier
rf= RandomForestClassifier(max_depth=2,n_estimators=100,max_features="sqrt")    #max_depth=log(no of features)
rf.fit(x_train, y_train)
y_pred= rf.predict(x_test)

#doing cross validation to get best value of max _depth to prevent overfitted model 
from sklearn.model_selection import cross_val_score 
from sklearn.ensemble import RandomForestClassifier
for depth in [1,2,3,4,5,6,7,8,9,10]:
  rf= RandomForestClassifier(max_depth=depth,n_estimators=100,max_features="sqrt")   # will tell the DT to not grow past the given threhsold
  # Fit dt to the training set
  rf.fit(x_train, y_train) # the model is trained
  rf= RandomForestClassifier(max_depth=depth,n_estimators=100,max_features="sqrt")   # a fresh model which is not trained yet
  valAccuracy = cross_val_score(rf, x_train, y_train, cv=10) # syntax : cross_val_Score(freshModel,fts, target, cv= 10/5)
  print("Depth  : ", depth, " Training Accuracy : ", trainAccuracy, " Cross val score : " ,np.mean(valAccuracy))

"""**Depth = 8 is giving the good cross validation score fo 0.904**"""

from xgboost import plot_importance

# plot feature importance
plot_importance(model)
plt.show()

df.columns

"""f0 - Age, f1 - Job, f2 - marital status, f3- educational qualification, 
f4 - call type, f5 - day, f6 - mon, f7 -dur, f8 - number of calls, 
f9 - previous outcome f10 - y 

"""

