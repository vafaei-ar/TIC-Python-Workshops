class Test:
       
    def __init__(self,x):
        print('the init method is called.')
        print(x,'is taken as argument')
        self.x = x
        
    def __del__(self):
        print('delet method is called.')


t1 = Test(3)



