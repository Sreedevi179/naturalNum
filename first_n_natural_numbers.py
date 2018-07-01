#(sum of n1 natural numbers+n2 natural numbers....)

i=0
num=[]
sum1=0

print('Enter the number of parameters (n1,n2...) : ')
n=input()

print('Enter the parameters(Enter nothing to stop) : ')

while True:
    parameters=input()

    if parameters=='':
        break
    num=num+[parameters]

for parameters in num:
    
    sum=int(parameters)*(int(parameters)+1)/2
    sum1=sum1+sum

print('the answer is',sum1)
    
    
    
