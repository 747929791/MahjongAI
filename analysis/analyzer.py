#coding=utf-8
from functools import wraps
import inspect
import sys

def LogTrace(func):
    if '--stdio' in sys.argv:
        LogTrace.out=sys.stdout
    else:
        LogTrace.out=open('FuncTrace.log','w')
    LogTrace.FuncArgsList=[]  #if func.name in this list, print args
    print(inspect.getargspec(func))
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not hasattr(LogTrace,'level'):
            LogTrace.level=0
        LogLevel=''.join(['  ' for i in range(LogTrace.level)])
        LogStr=LogLevel+'I : '+func.__module__+'.'+func.__name__
        try:
            spec=inspect.getcallargs(func,*args,**kwargs)
            if 'self' in spec:
                spec.pop('self')
            LogStr+='  '+str(spec)
        except Exception:
            LogStr+='  ParseArgError'
        #LogTrace.out.write(LogStr+'\n')
        #print(inspect.getargspec(func))
        #print(inspect.getsource(func))
        LogTrace.level+=1
        ret = func(*args,**kwargs)
        LogTrace.level-=1
        LogStr=LogLevel+'O : '+func.__module__+'.'+func.__name__
        try:
            
            LogStr+='  '+str(ret)
        except Exception:
            LogStr+='  ParseRetError'
        #LogTrace.out.write(LogStr+'\n')
        LogTrace.out.flush()
        return ret
    
    return wrapper
    
def AnaLog(s,msg):
    if not hasattr(AnaLog,'out'):
        if '--stdio' in sys.argv:
            AnaLog.out=sys.stdout
        else:
            AnaLog.out=open('AnaMsg.log','w')
    AnaLog.out.write(s+' : '+str(msg)+'\n')
    AnaLog.out.flush()