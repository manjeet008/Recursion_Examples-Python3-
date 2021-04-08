def decimal1(num):
    if num==0:
        return(0)
    else:
        return(num%2+10*decimal1(int(num/2)))
input1=int(input("\nEnter a number.."))
print(decimal1(input1))

# Let's Take the example of num=5 here..
# The recursion function will be like
# 1+10x[0+10x[1+10x(0)]]
# 1+10x[0+10x[1+0]]
# 1+10x[0+10x1]
# 1+10x[0+10]
# 1+10x(10)
# 1+10x10
# 1+100
# 101 Final Output (The binary conversion of digit 5..)