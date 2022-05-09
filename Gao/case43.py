#模仿静态变量(static)另一案例
class Num:
    num = 10
    def screen(self):
        self.num += 1
        print("class num = %d" %self.num)
if __name__ == "__main__":
    num = 5
    a = Num()
    for i in range(3):
        num += 1
        print("global num = %d" %num)
        a.screen()