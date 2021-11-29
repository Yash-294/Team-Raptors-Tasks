class String:
    s=""
    def get_String(self):
        self.s=input("Enter String:")
    def print_String(self):
        print(self.s.upper())
d=String()
d.get_String()
d.print_String()