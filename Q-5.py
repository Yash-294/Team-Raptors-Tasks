class Roman:
    def romtoint(self):
        n=str(input("Enter the roman numeral you want to convert to integer:"))
        a={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":40,"I":1}
        r=0
        s=len(n)
        i=s-1
        for  i in range(len(n)):
            if i+1!=len(n) and a[n[i]]<a[n[i]]:
                r=r-a[n[i]]
            else:
                r=r+a[n[i]]
        print(r)
r=Roman()
r.romtoint()