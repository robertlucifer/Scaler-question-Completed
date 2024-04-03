inp=int(input("enter a the number"))
for i in range (inp):
    med=inp-i-1
    last=2*i+1
    print(' '*med,"*"*i,''*last)