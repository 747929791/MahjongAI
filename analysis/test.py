#coding=utf-8
from analyzer import *

class A():
    @LogTrace
    def __init__(self,b=2):
        self.b=2
    @LogTrace
    def q(self,a):
        return g(a)
    def __call__(self):
        print(self)

class B():
    f=A()

@LogTrace
def f(a,b=0,*c,**d):
    return g(a-1)+g(a-2)
    
@LogTrace
def g(a):
    return h(a-1)+h(a-2)


@LogTrace
def p():
    pass
    
@LogTrace
def h(a):
    p()
    if a<2: return 1
    return h(a-1)+h(a-2)
    
def _decorator(foo):
    def magic( self ) :
        print("start magic")
        foo( self )
        print("end magic")
    return magic
    
class Test(object):

    @_decorator
    def bar( self ) :
        print("normal call")

test = Test()

test.bar()

if __name__=='__main__':
    a=A()
    a.q(5)
    #print(f(5))
    AnaLog(['123','456'])