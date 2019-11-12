a=int(input("enter a student"))
b=int(input("enter number of apple"))
if b>=a:
    d=b//a
    print("the apple which each student is:" +str(d))
    s= b-(a*d)
    print(s)
else:
    print('The no. of students is more. Please enter values again')
