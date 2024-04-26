

def squaresum(a):
    sum=0
    if(a>0):
        print("printing the sum series sequence")
        for i in range(1,a+1):
            sum= sum + i*i
            print(i,sum)
    else:
        print("invalid input")
    print("The sum of square series of",a,"th natural number is",sum)
a=int(input("Enter the number series:"))
squaresum(a)



