import sys,os
l=['get','like','you','i','x']
d={'like':4}
dbname,verb,a,b,c=(l[0:]+[None])[:5]
print(dbname+" ",verb+" ",a+" ",b +" ",c +" ")
a=input("Enter key:")
try:
    print(d[a])
except KeyError:

    print("Key does not exist",file=sys.stderr)
    sys.stderr.write("Key does not exist\n")
