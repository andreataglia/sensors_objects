%matplotlib inline
import numpy as np
import pandas as pd

ver=pd.read_csv("data/data_out.csv")

ver.loan_purpose_name.value_counts().plot(kind='barh')



import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import pandas as pd

data=pd.read_csv("data_out.csv")
data.loc[:,['x','y','z']]
data['x']

X = [] # images
y = [] # labels
y = ver.loc[:,['obj']]
ROWS = 4
arr = []
arr.append(ver.loc[0,['x','y','z']])
X.append(ver.loc[0:3,['x','y','z']])
X.append(ver.loc[4:7,['x','y','z']])
X[1]

#for i in range(0, 2):
    #X.append(ver.loc[(i*ROWS)+1:((i+1)*ROWS),['x','y','z']])
#Lets view some of the pics
plt.figure(figsize=(10,5))
columns = 3
plt.subplot(5 / columns + 1, columns, 1 + 1)
plt.imshow(X[0])
plt.subplot(5 / columns + 1, columns, 2 + 1)
plt.imshow(X[1])