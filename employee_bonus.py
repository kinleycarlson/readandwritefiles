import csv

infile = open('EmployeePay.csv','r')
csvfile = csv.reader(infile, delimiter = ',')
next(csvfile)

for record in csvfile:
    pay = float(record[3])
    bonus = float(record[4])
    total_pay = pay + bonus*pay
    print('ID:',record[0])
    print('fname: ',record[1])
    print('lname: ', record[2])
    print('Total Pay: ', str(total_pay))

    input()

infile.close()



