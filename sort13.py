import random
n=15
a=[0]*n
print(a)
for i in range(len(a)):
    a[i]=random.randint(1,1000)

print(a)

for i in range(n):
    for j in range(n-i-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
print(a)
