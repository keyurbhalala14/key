a,b=int(input("Enter the number")),1
while True:
    for i in range(a*1,a*11,a):
        print(a,"*",b,"=",i)
        b+=1
    a= int(input("Enter next number: "))