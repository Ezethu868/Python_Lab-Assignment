#START
#get num1
#get num2
#if num2 !=0 and num1 !=0
#    print num1/num2
#else
#    print "Error: division by zero"
#End

num1=float(input("Enter the integer:"))
num2=float(input("Enter the second integer:"))

if num2 !=0 and num1 !=0:
    print("num1 is a multiple of ",num2)
else:
    print("num1 is not a multiple of ",num2)