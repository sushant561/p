GE (ELECTRONICS) DATA ENGINEERING AND ANALYTICS 
PRACTICAL 
NAME: SUSHANT BHAGAT 
ROLL NO: 24/48068 
COURSE: B.SC (HONS.) COMPUTER SCIENCE 1ST SEM 
SUB: GE (ELECTRONICS) DATA ENGINEERING AND ANALYTICS 
CO1 : Implement various data analysis tools in the pandas library. 
import pandas as pd 
import numpy as np 
# user data  
data = { 
'name': ['sanjay', 'sushant', 'shashi','roshni', 'rahul', 'pankaj'], 
'age': [20,18,19,20,21,22], 
'gender' : ['M','M','M','F','M','M'], 
'sports' : ['bgmi', 'gta-v', 'football', 'ludo', 'cricket', 'chess'] 
} 
df = pd.DataFrame(data) 
# print all data  
print(df) 
name  age gender    sports 
0   sanjay   20      M      bgmi 
1  sushant   18      M     gta-v 
2   shashi   19      M  football 
3   roshni   20      F      ludo 
4    
rahul   21      M   cricket 
5   pankaj   22      M     chess 
# print all columns name 
column_name = df.columns 
print(column_name) 
Index(['name', 'age', 'gender', 'sports'], dtype='object') 
# print top 3 columns 
top_3 = df.head(3) 
print(top_3)  
name  age gender    sports 
0   sanjay   20      M      bgmi 
1  sushant   18      M     gta-v 
2   shashi   19      M  football 
# print last 3 column  
last_3 = df.tail(3) 
print(last_3) 
name  age gender   sports 
3  roshni   20      
F     ludo 
4   rahul   21      
M  cricket 
5  pankaj   22      M    chess 
# show only one column that is name  
names_col = df['name'] 
print(names_col) 
0     
sanjay 
1    
sushant 
2     
shashi 
3     
roshni 
4      
rahul 
5     
pankaj 
# show only 3rd index row  
third_rw = df.loc[3] 
print(third_rw) 
name      Roshni 
age           
20 
gender         
F 
sports      
ludo 
Name: 3, dtype: object 
# add one more column to data  
df['fav_movie'] = ['war', 'MI', 'interstaller', 'pushpa', 'stree2', 'avengers'] 
print(df) 
name  age gender    sports     fav_movie 
0   sanjay   20      M      bgmi           
war 
1  sushant   18      M     gta-v            
MI 
2   shashi   19      M  football  interstaller 
3   roshni   20      F      ludo        pushpa 
4    
rahul   21      M   cricket        stree2 
5   pankaj   22      M     chess      avengers 
# change indexing 
df = pd.DataFrame(data, index=['one', 'two', 'three', 'four', 'five', 'six']) 
print(df) 
name  age gender    sports 
one     sanjay   20      M      bgmi 
two    sushant   18      M     gta-v 
three   shashi   19      M  football 
four    roshni   20      F      ludo 
f
 ive     
rahul   21      M   cricket 
six     
pankaj   22      
M     chess 
CO2 : Implement various basic data analysis techniques, clean and filter and 
manipulate data. 
import pandas as pd 
import numpy as np 
data = { 
'name': ['sanjay', 'sushant', 'shashi','roshni', 'rahul', 'pankaj'], 
'age': [20,18,19,20,None,22], 
'gender' : ['M','M','M','F','M','M'], 
'sports' : ['bgmi', 'gta-v', 'football', None, 'bgmi', None] 
} 
df = pd.DataFrame(data) 
# basic information about data  
df_info = df.describe() 
print(df_info) 
           age 
count   5.00000 
mean   19.80000 
std     1.48324 
min    18.00000 
25%    19.00000 
50%    20.00000 
75%    20.00000 
max    22.00000 
 
# Check for missing values 
missing_data = df.isnull().sum() 
print(missing_data) 
 
name      0 
age       1 
gender    0 
sports    2 
 
# Fill missing age values with the mean age value 
mean_age = df['age'].mean() 
df['age'] = df['age'].fillna(mean_age) 
age_col = df['age'] 
print(age_col) 
0    20.0 
1    18.0 
2    19.0 
3    20.0 
4    19.8 
5    22.0 
 
# Fill missing sport values with Unknown 
df['sports'] = df['sports'].fillna('Unknown') 
sport_col = df['sports'] 
print(sport_col) 
0        bgmi 
1       gta-v 
2    football 
3     Unknown 
4        bgmi 
5     Unknown 
 
# Filter rows where age > 19 
filtered_age = df[df['age'] > 19] 
print(filtered_age) 
     name   age gender sports 
0  sanjay  20.0      M   bgmi 
3  roshni  20.0      F   None 
5  pankaj  22.0      M   None 
# Add a new column indicating if the person is above 30 years old 
df['is_above_30'] = df['age'] > 19 
print(df) 
      name   age gender    sports  is_above_30 
0   sanjay  20.0      M      bgmi         True 
1  sushant  18.0      M     gta-v        False 
2   shashi  19.0      M  football        False 
3   roshni  20.0      F      None         True 
4    rahul   NaN      M      bgmi        False 
5   pankaj  22.0      M      None         True 
# Count the number of participants in each sport 
sport_count = df.groupby('sports')['name'].count() 
print(sport_count) 
Sports 
bgmi        2 
football    1 
gta-v       1 
# Sort by age in descending order 
sorted_data = df.sort_values('age', ascending=True) 
print(sorted_data) 
1  sushant  18.0      M     gta-v 
2   shashi  19.0      M  football 
0   sanjay  20.0      M      bgmi 
3   roshni  20.0      F      None 
5   pankaj  22.0      M      None 
4    rahul   NaN      M      bgmi 
 
 
CO3 : Solve real world data analysis problems 
1 . Create a Data Frame and perform Matrix-like Operations on a Data Frame 
import pandas as pd 
import numpy as np 
data = { 
'A': [1, 2, 3], 
'B': [4, 5, 6], 
'C': [7, 8, 9] 
} 
data_2 = { 
'A': [9, 8, 7], 
'B': [6, 5, 4], 
'C': [3, 2, 1] 
} 
df = pd.DataFrame(data) 
df_2 = pd.DataFrame(data_2) 
# Transpose matrix 
df_transposed = df.T 
print(df_transposed) 
Output: 
1  2 3 
4  5  6 
7  8  9 
# Additioin 
df_add = df + df_2 
print(df_add) 
Output: 
10  10  10 
10  10  10 
10  10  10 
#Subtraction 
df_subtract = df - df_2 
print(df_subtract) 
Output: -8 -2  4 -6  0  6 -4  2  8 
# Matrix Multiplication (Dot Product) 
df_dot = df.dot(df_2.T) 
print(df_dot) 
Output: 
54  42  30 
72  57  42 
90  72  54 
# Element-wise Multiplication 
df_elementwise = df * df_2 
print(df_elementwise) 
Output 
9 24 21 
16 25 16 
21 24 9 
# Element-wise Division 
df_division = df / df_2 
print(df_division) 
Output 
0.111111    0.666667    2.333333 
0.250000    1.000000    4.000000 
0.428571   1.500000     9.000000 
2. Implement basic array statistical methods (sum, mean, std, var, min, max, 
argmin, argmax, cumsum and cumprod) and perform sorting operation with 
sort method. 
import numpy as np 
arr = np.array([10, 20, 15, 30, 25]) 
print(arr) 
[10 20 15 30 25] 
# Sum of all element in array 
arr_sum = np.sum(arr) 
print(arr_sum) 
100 
# Mean of the array 
arr_mean = np.mean(arr) 
print(arr_mean) 
20.0 
# Standard deviation of the array 
arr_std = np.std(arr) 
print(arr_std) 
7.0710678118654755 
# Variance of the array 
arr_var = np.var(arr) 
print(arr_var) 
50.0 
# Minimum value in the array 
arr_min = np.min(arr) 
print(arr_min) 
10 
# Maximum value in the array 
arr_max = np.max(arr) 
print(arr_max) 
30 
# Index of the minimum value 
arr_argmin = np.argmin(arr) 
print(arr_argmin) 
0 
# Index of the maximum value 
arr_argmax = np.argmax(arr) 
print(arr_argmax) 
3 
# Cumulative sum 
arr_cumsum = np.cumsum(arr) 
print(arr_cumsum) 
[ 10  30  45  75 100] 
# Cumulative product 
arr_cumprod = np.cumprod(arr) 
print("Cumulative Product:", arr_cumprod) 
[     
10     200    3000   90000 2250000] 
# Sort the array and store value 
sorted_arr = np.sort(arr) 
print(sorted_arr) 
[10 15 20 25 30] 
# Sort the original array  
arr.sort() 
print(arr) 
[10 15 20 25 30] 
3. Create a data frame with a following structure using pandas 
import pandas as pd 
data = {   
'EMP ID': [1,2,3,4,5], 
'EMP NAME': ['Satish', "Reeya", "Jay", 'Roy', "Serah"], 
'EMP SALARY': [50000,75000,100000,45000,55000], 
'START DATA': ['01-11-2017', '12-05-2016', '22-09-2015', '08-01-2017', '06-02-2018'] 
} 
df = pd.DataFrame(data) 
print(df) 
EMP ID EMP NAME  EMP SALARY  START DATA 
0       
1      Satish         50000         01-11-2017 
1       
2      Reeya         
75000         
12-05-2016 
2       
3      Jay               
100000      
22-09-2015 
3       
4      Roy              
45000        
08-01-2017 
4       
5      Serah           
55000        
06-02-2018 
CO4 : Load Pima Indians Diabetes dataset 
(Source:https://archive.ics.uci.edu/ml/datasets/diabetes). Implement the 
following 
(i) . Data Cleaning and Filtering methods (Use NA handling methods, fillna 
function arguments). 
import pandas as pd 
import numpy as np 
df = pd.read_csv('BostonHousing.csv') 
print(df) 
crim    zn  indus  chas    nox     rm   age     dis  rad  tax  ptratio       b  lstat  medv 
0    
0.00632  18.0   2.31     0  0.538  6.575  65.2  4.0900    1  296     15.3  396.90   4.98  24.0 
1    
0.02731   0.0   7.07     0  0.469  6.421  78.9  4.9671    2  242     17.8  396.90   9.14  21.6 
2    
0.02729   0.0   7.07     0  0.469  7.185  61.1  4.9671    2  242     17.8  392.83   4.03  34.7 
3    
0.03237   0.0   2.18     0  0.458  6.998  45.8  6.0622    3  222     18.7  394.63   2.94  33.4 
4    
0.06905   0.0   2.18     0  0.458  7.147  54.2  6.0622    3  222     18.7  396.90   5.33  36.2 
..       ...   ...    ...   ...    ...    ...   ...     ...  ...  ...      ...     ...    ...   ... 
501  0.06263   0.0  11.93     0  0.573  6.593  69.1  2.4786    1  273     21.0  391.99   9.67  22.4 
502  0.04527   0.0  11.93     0  0.573  6.120  76.7  2.2875    1  273     21.0  396.90   9.08  20.6 
503  0.06076   0.0  11.93     0  0.573  6.976  91.0  2.1675    1  273     21.0  396.90   5.64  23.9 
504  0.10959   0.0  11.93     0  0.573  6.794  89.3  2.3889    1  273     21.0  393.45   6.48  22.0 
505  0.04741   0.0  11.93     0  0.573  6.030  80.8  2.5050    1  273     21.0  396.90   7.88  11.9 
 
 
 
# Check for missing values 
print(df.isnull().sum()) 
crim       0 
zn         0 
indus      0 
chas       0 
nox        0 
rm         0 
age        0 
dis        0 
rad        0 
tax        0 
ptratio    0 
b          0 
lstat      0 
medv       0 
dtype: int64 
 
# Display rows with missing values 
print(df[df.isnull().any(axis=1)]) 
Empty DataFrame 
Columns: [crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat, medv] 
Index: [] 
 
# Fill missing values in numeric columns with their mean 
crim_mean = df['crim'].mean() 
indus_mean = df['indus'].mean() 
df['crim'] = df['crim'].fillna(crim_mean) 
df['indus'] = df['indus'].fillna(indus_mean) 
 
# Fill missing values in 'chas' with 0  
df['chas'] = df['chas'].fillna(0) 
 
(ii) Implement descriptive and summary statistics. 
# Summary statistics for the entire dataset 
summary_stats = df.describe() 
print(summary_stats) 
             crim          zn       indus        chas         nox          rm  ...         rad         tax     ptratio           b       
lstat        medv 
count  506.000000  506.000000  506.000000  506.000000  506.000000  506.000000  ...         
506.000000  506.000000  506.000000  506.000000  506.000000  506.000000 
mean     3.613524   11.363636   11.136779    0.069170    0.554695    6.284634  ...    9.549407  
408.237154   18.455534  356.674032   12.653063   22.532806 
std      8.601545   23.322453    6.860353    0.253994    0.115878    0.702617  ...    8.707259  
168.537116    2.164946   91.294864    7.141062    9.197104 
min      0.006320    0.000000    0.460000    0.000000    0.385000    3.561000  ...    1.000000  
187.000000   12.600000    0.320000    1.730000    5.000000 
25%      0.082045    0.000000    5.190000    0.000000    0.449000    5.885500  ...    4.000000  
279.000000   17.400000  375.377500    6.950000   17.025000 
50%      0.256510    0.000000    9.690000    0.000000    0.538000    6.208500  ...    5.000000  
330.000000   19.050000  391.440000   11.360000   21.200000 
75%      3.677083   12.500000   18.100000    0.000000    0.624000    6.623500  ...   24.000000  
666.000000   20.200000  396.225000   16.955000   25.000000 
max     88.976200  100.000000   27.740000    1.000000    0.871000    8.780000  ...   
24.000000  711.000000   22.000000  396.900000   37.970000   50.000000 
 
[8 rows x 14 columns] 
# Mean 
mean_values = df.mean() 
print(mean_values) 
crim         3.613524 
zn          11.363636 
indus       11.136779 
chas         0.069170 
nox          0.554695 
rm           6.284634 
age         68.574901 
dis          3.795043 
rad          9.549407 
tax        408.237154 
ptratio     18.455534 
b          356.674032 
lstat       12.653063 
medv        22.532806 
dtype: float64 
 
# Median 
median_values = df.median() 
print(median_values) 
crim         0.25651 
zn           0.00000 
indus        9.69000 
chas         0.00000 
nox          0.53800 
rm           6.20850 
age         77.50000 
dis          3.20745 
rad          5.00000 
tax        330.00000 
ptratio     19.05000 
b          391.44000 
lstat       11.36000 
medv        21.20000 
dtype: float64 
 
# Standard Deviation 
std_values = df.std() 
print(std_values) 
crim         8.601545 
zn          23.322453 
indus        6.860353 
chas         0.253994 
nox          0.115878 
rm           0.702617 
age         28.148861 
dis          2.105710 
rad          8.707259 
tax        168.537116 
ptratio      2.164946 
b           91.294864 
lstat        7.141062 
medv         9.197104 
dtype: float64 
# Variance 
var_values = df.var() 
print(var_values) 
crim          73.986578 
zn           543.936814 
indus         47.064442 
chas           0.064513 
nox            0.013428 
rm             0.493671 
age          792.358399 
dis            4.434015 
rad           75.816366 
tax        28404.759488 
ptratio        4.686989 
b           8334.752263 
lstat         50.994760 
medv          84.586724 
dtype: float64 
 
(iii) Plot histogram, bar plot, distplot for features/attributes of the dataset 
import matplotlib.pyplot as plt 
import seaborn as sns 
# Plot histogram for the 'medv' column 
plt.figure(figsize=(8, 6)) 
plt.hist(df['medv'], bins=20, color='skyblue', edgecolor='black') 
plt.title('Histogram of medv', fontsize=16) 
plt.xlabel('medv', fontsize=14) 
plt.ylabel('Frequency', fontsize=14) 
plt.grid(axis='y', alpha=0.75) 
plt.show() 
# Plot bar plot for the mean values of columns 
mean_values = df.mean() 
plt.figure(figsize=(10, 6)) 
mean_values.plot(kind='bar', color='lightgreen', edgecolor='black') 
plt.title('Mean Values of Features', fontsize=16) 
plt.xlabel('Features', fontsize=14) 
plt.ylabel('Mean Value', fontsize=14) 
plt.xticks(rotation=45, ha='right') 
plt.show() 
# Distplot for 'rm' column 
plt.figure(figsize=(8, 6)) 
sns.histplot(df['rm'], kde=True, bins=20, color='purple') 
plt.title('Distribution of rm', fontsize=16) 
plt.xlabel('rm', fontsize=14) 
plt.ylabel('Density', fontsize=14) 
plt.show() 
CO5 : Load Boston Housing Price dataset and perform: 
Plot 'distplot' for target variable and 'heatmap' for the correlation in dataset. 
import pandas as pda 
import seaborn as sns 
import matplotlib.pyplot as plt 
df = pd.read_csv("BostonHousing.csv") 
plt.figure(figsize=(8, 6)) 
sns.histplot(df['medv'], kde=True, color='blue', bins=20) 
plt.title('Distribution of MEDV (Target Variable)', fontsize=16) 
plt.xlabel('MEDV ($1000)', fontsize=14) 
plt.ylabel('Frequency', fontsize=14) 
plt.show() 
# Compute the correlation matrix 
correlation_matrix = df.corr() 
# Plot the heatmap 
plt.figure(figsize=(12, 8)) 
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5) 
plt.title('Correlation Heatmap', fontsize=16) 
plt.show() 
CO 6. For above data set, perform grouping the data using index in pivot 
table, aggregate on specific features with values. 
import pandas as pd 
df = pd.read_csv('BostonHousing.csv') 
# Pivot table grouped by 'chas' and aggregated on 'medv' and 'rm' 
pivot_table = pd.pivot_table( 
df, 
values=['medv', 'rm'],     
# Columns to aggregate 
index='chas',              
# Index for grouping 
aggfunc={'medv': 'mean',   # Mean of 'medv' 
'rm': 'sum'}      
# Sum of 'rm' 
) 
# Display the pivot table 
print("Pivot Table Grouped by 'chas':") 
print(pivot_table) 
Pivot Table Grouped by 'chas': 
chas           
medv        
rm 
0     
22.093843  2951.839 
1     
28.440000   228.186 
import matplotlib.pyplot as plt 
pivot_table['medv'].plot(kind='bar', figsize=(8, 6), color='skyblue', edgecolor='black') 
plt.title('Average MEDV by CHAS', fontsize=16) 
plt.xlabel('CHAS', fontsize=14) 
plt.ylabel('Average MEDV', fontsize=14) 
plt.xticks(rotation=0) 
plt.grid(axis='y', linestyle='--', alpha=0.7) 
plt.show() 
CO 7 . For Superstore sales data, perform Time Series Data Analysis. 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from statsmodels.tsa.seasonal import seasonal_decompose 
# Simulated Superstore Sales Data 
data = { 
"Order Date": pd.date_range(start="2021-01-01", periods=24, freq='M'),  # 24 months of 
data 
"Sales": [200, 250, 180, 300, 350, 400, 450, 500, 380, 420, 460, 550,  
600, 580, 560, 620, 700, 680, 640, 720, 750, 780, 820, 800] 
} 
# Create the DataFrame 
df = pd.DataFrame(data) 
# Convert 'Order Date' to datetime format  
df['Order Date'] = pd.to_datetime(df['Order Date']) 
# Set 'Order Date' as the index 
df.set_index('Order Date', inplace=True) 
# Preview the DataFrame 
print(df.head(3)) 
print(df.tail(3)) 
Sales 
Order Date        
2021-01-31    200 
2021-02-28    250 
2021-03-31    180 
Sales 
Order Date        
2022-10-31    780 
2022-11-30    820 
2022-12-31    800 
# Plot sales over time 
plt.figure(figsize=(12, 6)) 
plt.plot(df['Sales'], marker='o', color='blue', label='Sales') 
plt.title('Monthly Sales Over Time', fontsize=16) 
plt.xlabel('Month', fontsize=14) 
plt.ylabel('Sales', fontsize=14) 
plt.legend() 
plt.grid() 
plt.show() 
# Decompose the time series 
decomposition = seasonal_decompose(df['Sales'], model='additive', period=12) 
# Plot the decomposition 
decomposition.plot() 
plt.show() 
# Extract month from the index 
df['Month'] = df.index.month 
# Group by month and calculate average sales 
seasonality = df.groupby('Month')['Sales'].mean() 
# Plot seasonality 
plt.figure(figsize=(10, 6)) 
sns.barplot(x=seasonality.index, y=seasonality.values, palette='coolwarm') 
plt.title('Average Monthly Sales (Seasonality)', fontsize=16) 
plt.xlabel('Month', fontsize=14) 
plt.ylabel('Average Sales', fontsize=14) 
plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',  
'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45) 
plt.show() 