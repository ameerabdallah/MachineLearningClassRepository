#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: 1 hour
#-----------------------------------------------------------+

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
num_attributes = 4
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
# age:                      Young = 1, Prepresbyopic = 2, Presbyopic = 3
# Spectacle Prescription:   Myope = 1, Hypermetrope = 2
# astigmatism:              Yes = 1, No = 2
# Tear Production Rate:     Reduced = 1, Normal = 2
#--> add your Python code here
age = ['Young', 'Prepresbyopic', 'Presbyopic']
spectaclePrescription = ['Myope', 'Hypermetrope']
astigmatism = ['Yes', 'No']
tearProductionRate = ['Reduced', 'Normal']

attributes = []
attributes.append(age)
attributes.append(spectaclePrescription)
attributes.append(astigmatism)
attributes.append(tearProductionRate)


for i, row in enumerate(db):
  newRow = []
  for j, value in enumerate(row[:-1]):
    newRow.append(attributes[j].index(value) + 1)
  X.append(newRow)

print('\nX = ' + str(X))


#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here

for row in db:
  if row[-1] == 'Yes':
    Y.append(1)
  elif row[-1] == 'No':
    Y.append(2)
print('\nY = ' + str(Y))


#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['age', 'Spectacle', 'astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()


