class Math:
    def __init__(self,num):
        self.num = num
    
    def addtonum(self, n):
        self.num += n

    @staticmethod
    def add(a,b):
        return a+b

if __name__ == "__main__":      
    a = Math(10)
    print(a.num)
    a.addtonum(20)
    print(a.num)
    print(Math.add(10,20))
        