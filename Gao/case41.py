#模仿静态变量的用法
def varfunc():
    var = 0
    print("var is %d" % var)
    var += 1
print(varfunc())
if __name__ == "__main__":
    for i in range(3):
        varfunc()
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print (self.StaticVar)
print(Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()