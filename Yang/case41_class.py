def var():
    v=0
    print(v)
    v+=1
if __name__=='__main__':
    for i in range(3): var()

    
class var:
    v=0
    def varfunc(self):
        self.v+=1
        print(self.v)
a=var()
for i in range(3): a.varfunc()