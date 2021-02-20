#-------------------------------------------------------------------------
# AUTHOR: Ameer Abdallah
# FILENAME: Find_S
# SPECIFICATION: reads from file "contact_lens.csv and output the hypothesis of Find-S algorithm"
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here
first_hypothesis_index = 0

for i, row in enumerate(db):
  if db[i][4] == 'Yes':
    hypothesis = row[:-1]
    first_hypothesis_index = i
    break

print("\n Process of finding Maximally Specific Hypothesis")
print(hypothesis)


#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here

for row in db[first_hypothesis_index+1:]:
  # skip rows that have a negative class value
  if row[4] == 'No':
    continue

  # save a temporary hypothesis to compare against

  # iterate through new row
  for i, value in enumerate(row[:-1]):
    # if the value in the row corresponding the the value in the hypothesis are
    # not the same remove this specific feature value from the hypothesis by replacing
    # the value with a '?'
    if value != hypothesis[i]:
      hypothesis[i] = '?'

  print(hypothesis)

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)