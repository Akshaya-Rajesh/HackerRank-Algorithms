s,t=input().split(' ')
s=int(s)
t=int(t)
a,b=input().split(' ')
a=int(a)
b=int(b)
m,n=input().split(' ')
count_a=0
count_b=0
apple=list(map(int,input().split()))
orange=list(map(int,input().split()))
for i in apple:
    if(s<=a+i<=t):
        count_a+=1
for i in orange:
    if(s<=b+i<=t):
        count_b+=1
print(count_a)
print(count_b)
