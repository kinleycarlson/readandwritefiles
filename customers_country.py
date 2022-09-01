import csv

infile = open('customers.csv','r')

outfile = open('customer_country.csv','w')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile)

outfile.write('Full Name, Country' + '\n')
counter = 0
for record in csvfile:
    fname = record[1]
    lname = record[2]
    country = record[4]
    counter +=1
    outfile.write(fname + ' '+ lname+', '+ country+ '\n')
    
outfile.write('Total Number of Customers:'+ str(counter))


infile.close()
outfile.close()
