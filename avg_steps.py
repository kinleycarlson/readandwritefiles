import csv
infile = open('steps.csv','r')
csvfile = csv.reader(infile, delimiter = ',')
outfile = open('avg_steps.csv','w')
next(csvfile)


total_steps = 0
counter = 1
month = 1
for record in csvfile:
    if record[0] == month:
        total_steps += int(record [1])
        counter +=1
    else:
        avg_steps = format(total_steps/counter,'.2f') 
        print(avg_steps)
        month = record[0]
        print(month)
        outfile.write(month+ ', '+str(avg_steps)+'\n')
        counter = 1
        total_steps =0

infile.close()
outfile.close()
