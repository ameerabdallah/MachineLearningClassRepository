#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #5
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#importing some Python libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('trip_advisor_data.csv', sep=',', header=0) #reading the data by using the Pandas library ()

#iterate over the other 99 users to calculate their similarity with the active user (user 100) according to their category ratings (user-item approach)
# do this to calculate the similarity:
#vec1 = np.array([[1,1,0,1,1]])
#vec2 = np.array([[0,1,0,1,1]])
#cosine_similarity(vec1, vec2)
#do not forget to discard the first column (User ID) when calculating the similarities
#--> add your Python code here


del df['User ID']
sims = []
Y_Training = df[['galleries','restaurants']]

del df['galleries']
del df['restaurants']

X_Training = np.array(df)
Y_Training = np.array(Y_Training)

user100 = X_Training[-1]

for row in X_Training[:-1]:
   sims.append(cosine_similarity([user100], [row]))

#find the top 10 similar users to the active user according to the similarity calculated before
#--> add your Python code here

# reshape to be 1d
sims = np.reshape(sims, (len(sims)))

# top 10 similar users
users = (-sims).argsort()[:10]

#Compute a prediction from a weighted combination of selected neighbors’ for both categories evaluated (galleries and restaurants)
#--> add your Python code here

avg_u_100 = np.average(user100)
galleries_num = 0
rest_num = 0

denom = 0

for i in range(10):
   sim = sims[users[i]]
   denom += sim
   user_avg = np.average(X_Training[users[i]])


   # galleries_class
   galleries_num += sim*(float(Y_Training[users[i]][0])-user_avg)

   # rest_class
   rest_num += sim*(float(Y_Training[users[i]][1])-user_avg)
   

galleries_predict = avg_u_100 + (galleries_num/denom)
rest_predict = avg_u_100 + (rest_num/denom)

print("Galleries Prediction: "+str(galleries_predict))
print("Restaurant Prediction: "+str(rest_predict))