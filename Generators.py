#generators
#No tuple comprehension in above cases if we remove those braces,and keep paranthesis,then the outcome is generator
#A generator is also a function which can be used as an iterator(loop) by producing group of values where we use yield keyword
#yield vs return
#return will terminate the function where as yield can pass the function and go on with every succesive iteration.
#generators
'''a=[i**2 for i in range(16)]
print(a)
print(type(a))
'''
a=(i**2 for i in range(16))
print(a)
print(type(a))
print(*a)
'''
a=(i**2 for i in range(16))
#print(a)
#print(list(a))
#print(type(a))
#print(tuple(a))
print(set(a))'''

'''
a,b=[int(x) for x in input("enter the values").split(',')]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(',')]
def check(a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))'''

'''#yield vs return
def mygen():
    #return "python"
    #return "java"
    #return "html"
    return "python","java","html"
print(*mygen())'''

'''def mygen():
    yield "vja"
    yield "hyd"
    yield "vzg"
    yield "vja","hyd","vzg"
print(*mygen())

#next()-> is used to successive iteration
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))'''

def value():
    a=int(input("enter a"))
    b=int(input("enter b"))
    while a>b:
        a=a-1
        yield a
print(*value())



