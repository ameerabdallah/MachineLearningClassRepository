#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #4
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn.linear_model import Perceptron
import numpy as np
import pandas as pd

n = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]
r = [True, False]

df = pd.read_csv('optdigits.tra', sep=',', header=None) #reading the data by using Pandas library

X_training = np.array(df.values)[:,:64] #getting the first 64 fields to form the feature data for training
y_training = np.array(df.values)[:,-1]  #getting the last field to form the class label for training

df = pd.read_csv('optdigits.tes', sep=',', header=None) #reading the data by using Pandas library

X_test = np.array(df.values)[:,:64]    #getting the first 64 fields to form the feature data for test
y_test = np.array(df.values)[:,-1]     #getting the last field to form the class label for test

highest_accuracy = 0
for a in n: #iterates over n

    for b in r: #iterates over r

        accuracy = 0
        #Create the perceptron classifier
        clf = Perceptron(eta0=a, random_state=b, max_iter=1000) #eta0 = learning rate, random_state = used to shuffle the training data

        #Fitperceptron to the training data
        clf.fit(X_training, y_training)

        #make the classifier prediction for each test sample and start computing its accuracy
        #hint: to iterate over two collections simultaneously with zip() Example:
        #for (x_testSample, y_testSample) in zip(X_test, y_test):
        #to make a prediction do: clf.predict([x_testSample])
        #--> add your Python code here
        for (x_testSample, y_testSample) in zip(X_test, y_test):
            pred = int(clf.predict([x_testSample])[0])
            if pred == int(y_testSample):
                accuracy += 1
        accuracy = accuracy / len(X_test)


        #check if the calculated accuracy is higher than the previously one calculated. If so, update the highest accuracy and print it together with the perceprton hyperparameters
        #Example: "Highest Perceptron accuracy so far: 0.88, Parameters: learning rate=00.1, random_state=True"
        #--> add your Python code here
        if accuracy > highest_accuracy:
            highest_accuracy = accuracy
            print("Highest Perceptron accuracy so far: " + str(highest_accuracy) + ", Parameters: learning rate="+str(a)+", random_state="+str(b))










