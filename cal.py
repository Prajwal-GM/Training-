class Calculator:
    def _init_(self,a,b):
        self.a=a
        self.b=b
        print("im a default constructor..")
             def add(a,b):
              return a+b
             def sub(a,b):
              return a-b
             def mul(a,b):
              return a*b
             def div(a,b):
              return a/b
              
        obj1=Calculator
        obj2=Calculator
        obj3=Calculator
        print(obj1.add(4,9))
        print(obj2.sub(10,5))
        ans=obj3.mul(10,3)
        print(ans)
        
