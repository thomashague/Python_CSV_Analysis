import os 
import csv
import random

#get path of file
csvPath = input('What is the path of the input file you want to use? ex: budget_data_2.csv ')

#create rowCount variable
rowCount = 0
#create revenue sum variable
revenueSum = 0
oldValue = 0
#create revenue change array
revenueChange = 0
avgChange = 0
firstRow = True
newValue = 0
changes = []
changeSum = 0
biggestGainSoFar = 0
biggestLossSoFar = 0
increaseDate = 'null'
decreaseDate = 'null'


with open(csvPath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None) #skip the headers
    
    #find total months, the total revenue, and add the monthly changes in revenue to changes array
    for row in csvreader:
        newValue = int(row[1])
        #special case when starting (there's no change in revenue in first row)
        if(firstRow == True):
            oldValue = int(row[1])
        #get the change in revenue from this month to last month
        revenueChange = newValue - oldValue
        #keep track of biggest gains and losses in revenue
        if(revenueChange>biggestGainSoFar):
            biggestGainSoFar = revenueChange
            increaseDate = row[0] 
        if(revenueChange<biggestLossSoFar):
            biggestLossSoFar = revenueChange
            decreaseDate = row[0]
        #add changes in revenue to array, used for sum and average
        changes.append(revenueChange)
        #set old value to current row
        oldValue = int(row[1])
        #keep track of revenue sum
        revenueSum = revenueSum + int(row[1])
        #remove special condition since we've gone through one iteration
        firstRow = False
        rowCount = rowCount + 1
    
    #loop through change array to get total change sum
    for x in changes:
        changeSum = changeSum + int(x)
 
    avgChange = round(changeSum/(len(changes)-1),2)


    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(rowCount))
    print("Total Revenue: $" + str(revenueSum))
    print("Average Revenue Change: $" + str(avgChange))
    print("Greatest Increase in Revenue: " + str(increaseDate) + " " + "($" + str(biggestGainSoFar) + ")")
    print("Greatest Decrease in Revenue: " + str(decreaseDate) +  " " + "($" + str(biggestLossSoFar)+ ")")

line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = "Total Months: " + str(rowCount)
line4 = "Total Revenue: $" + str(revenueSum)
line5 = "Average Revenue Change: $" + str(avgChange)
line6 = "Greatest Increase in Revenue: " + str(increaseDate) + " " + "($" + str(biggestGainSoFar) + ")"
line7 = "Greatest Decrease in Revenue: " + str(decreaseDate) +  " " + "($" + str(biggestLossSoFar)+ ")"


#export to text file
outputPath = 'theresNoWayYouHaveaFileWithThisName' + str(random.randint(0,1000)) + '.txt'
f = open(outputPath,'w')
f.write(line1 + "\n")
f.write(line2 + "\n")
f.write(line3+ "\n")
f.write(line4+ "\n")
f.write(line5+ "\n")
f.write(line6+ "\n")
f.write(line7+ "\n")
f.close()




