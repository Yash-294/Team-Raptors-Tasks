class subset:
    def findsubset(self, s):
        print(self.subset2([], s))
    def subset2(self, t, s):
        if s:
            return self.subset2(t, s[1:]) + self.subset2(t + [s[0]], s[1:])
        return [t]
s1=subset()
s=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    x=input()
    s.append(x)
s1.findsubset(s)
