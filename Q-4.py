class Roman:
    def inttorom(self):
        n=int(input("Enter the number you want to convert to roman numeral:"))
        a={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":40,"I":1}
        r=""
        for s,v in a.items():
            while n>0:
                if v<=n:
                    r+=s
                    n-=v
                else:
                    break
        print(r)
r=Roman()
r.inttorom()