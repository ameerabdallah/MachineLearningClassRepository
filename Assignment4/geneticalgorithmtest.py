
def printTable(label, table):
    for i, row in enumerate(table):
        print(label +" "+ str(i+1) + ": "+ str(row))
        print()


dataset = [ [1,0,0,1,0,0,0],
            [0,1,0,0,0,1,1],
            [0,1,0,1,0,0,1],
            [0,0,1,0,0,1,0],
            [0,1,0,0,1,0,1],
]
chromosomes = [ [1,0,1,1,1,0,0],
                [1,0,1,1,1,0,0],
                [1,0,1,1,0,0,0],
                [1,0,1,1,0,1,0],
]

allchromosometraining =[]
chromosometraining = []
for rowi in chromosomes:
    chromosometraining = []
    #compare chromosome to dataset
    for i, rowj in enumerate(dataset):
        temp_row = []

        for j, d in enumerate(rowj[:-1]):
            temp_row.append(d & rowi[j])
        temp_row.append(int(rowj[-1] == rowi[-1]))

        outlook_result = (temp_row[0] | temp_row[1] | temp_row[2])
        temperature_result = (temp_row[3] | temp_row[4] | temp_row[5])
        playTennis_result = temp_row[6]

        chromosometraining.append((outlook_result & temperature_result) == playTennis_result)

    # calculate accuracy of last chromosome
    accuracy = 0
    for i in range(5):
        if chromosometraining[i] == 1:
            accuracy += 1
    accuracy = accuracy/5

    print(chromosometraining)
    # append accuracy of chromosome to dataset
    allchromosometraining.append(accuracy)

printTable("Chromosome Fitness",allchromosometraining)

pr = []
s = sum(allchromosometraining)
for i in range(len(allchromosometraining)):
    pr.append(allchromosometraining[i]/s)

printTable("Prediction", pr)