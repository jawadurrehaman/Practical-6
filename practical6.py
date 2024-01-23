fh = open('practical6.txt','w')
a=int(input("Enter a:")) 
fact=1 
while(a>1): 
    fact=fact*a 
    a=a-1 
fh.write(str(fact))
fh.close()