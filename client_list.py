def main():
    infile = open('clients.txt','r')
    count = 1 
    for line in infile:
        name = line.rstrip('\n')
        print(str(count),'. ', name, sep = '')
        count = int(count)+1

    infile.close()

main()

## counter = 1
## for line in infile
   ## print(counter, '. ',line.rstrip('\n'))
  ## counter +=1