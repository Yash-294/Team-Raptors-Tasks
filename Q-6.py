class specificsum:
    def sum(self,a,s):
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                if a[i]+a[j]==s:
                    print(i+1,",",j+1)

b=[]
s=int(input("Enter Specific Sum:"))
n=int(input("Enter number of elements in array:"))
print("Enter Elements:")
for i in range(0,n):
    x=int(input())
    b.append(x)
w=specificsum()
w.sum(b,s)