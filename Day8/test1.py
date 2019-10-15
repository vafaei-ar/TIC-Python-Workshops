class Test:
    def __new__(self,*args,**kwargs):
        print('the new method is called.')
        x = super().__new__(self)
        return x
        
    def __init__(self,x):
        print('the init method is called.')
        print(x,'is taken as argument')
        self.x = x
        
    def __del__(self):
        print('delet method is called.')


t1 = Test(3)



