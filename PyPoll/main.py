import os
import csv
import random

#NOTE: change this path depending on what data file you want to use
csvPath = input('What is the path of the input file you want to use? ex: election_data_1.csv')

rowCount = 0
candidate = 'Bob'
candidateArray = []
percentageArray = []
candidateStringArray = []
dummy = 0
candidateDictionary = {}
Winner = 'Bob'
mostSoFar = 0
candidateCounter = 0

with open(csvPath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None) #skip the headers

    for row in csvreader:
        rowCount = rowCount + 1
        candidate = str(row[2])
        if(candidate in candidateDictionary):
            candidateDictionary[candidate][0] = candidateDictionary[candidate][0] + 1 #do something to satisfy the computer...
        else:
            candidateDictionary[candidate] = [0,0]
            candidateDictionary[candidate][0] = 1 #add the candidate to the array

    for x in candidateDictionary:
        candidateDictionary[x][1] = ( ((candidateDictionary[x][0])/rowCount)*100)

    for x in candidateDictionary:
        if(candidateDictionary[x][1] > mostSoFar):
            mostSoFar = candidateDictionary[x][1]
            winner = x
        else:
            dummy = 0
            #do nothing


        
print(rowCount)
print(candidateDictionary)
print(winner)


line1 = "Election Results"
line2 = "-------------------------"
line3 = "Total Votes: " + str(rowCount)
line4 = "-------------------------"
for x in candidateDictionary:
    candidateStringArray.append(x + ": " + str(candidateDictionary[x][1])+ "% (" + str(candidateDictionary[x][0]) + ")" )

line5 = "-------------------------"
line6 = "Winner: " + winner
line7 = "-------------------------"


print(line1)
print(line2)
print(line3)
print(line4)
for x in candidateStringArray:
    print(x)
print(line5)
print(line6)
print(line7)

outputPath = 'theresNoWayYouHaveaFileWithThisName' + str(random.randint(0,1000)) + '.txt'
f = open(outputPath,'w')
f.write(line1 + "\n")
f.write(line2 + "\n")
f.write(line3+ "\n")
f.write(line4+ "\n")
for x in candidateStringArray:
    f.write(x + "\n")
f.write(line5+ "\n")
f.write(line6+ "\n")
f.write(line7+ "\n")
f.close()

