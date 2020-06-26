import csv

def main():

    inputCsvFileName = 'inputFile.csv'       # Name of input file
    outputFileName = 'dataOutputFile.txt'  # Name of output file

    print("Creating text file.")
    
    outFile = open(outputFileName, 'a')

    print("Connecting to CSV file file.")
    
    with open(inputCsvFileName, newline='') as csvFile:
        spamreader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        
        for row in spamreader:
           myData = (','.join(row))
           outFile.write(myData + '\n')
           
    print("Closing files")
    csvFile.close()
    outFile.close()

main()
