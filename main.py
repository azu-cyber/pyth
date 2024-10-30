def f1(n):
    return n*(n+1)/2
print(f1(4))
#the no. of iterations is 1
def f2(n):
    sum=0
    for i in range(1, n+1):
        sum+=i
    return sum
print(f2(4))
#the no. of iterations is 4
def fun3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum+=1
    return sum
print(fun3(4))
#the no. of iterations is 10