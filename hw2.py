import scipy
import numpy
def main():
    '''
    Print out two tables
    '''

    print 'Binomial Distribution Table:','\n'
    OutputBinomial()
    print 'Poisson Distribution Table:','\n'
    OutputPoisson()

    
def OutputBinomial():
    '''
    ()->table

    Output Binomial Distribution table
    '''
    print 'n','\t','t',' ',
    for i in range(1,10,1):
        j=i*0.1
        print j,'  ',
    print'\n'
    for n in range(5,21,1):
        print n,
        for t in range(0,6,1):
            print '\t',t,
            for p in range(1,10,1):
                q=p*(0.1)
                print '%01.4f'%(Binomial(n,t,q)),
            print '\n'


def Binomial(n,t,p):
    '''
    (float,float,float)->float

    RETURN value of Binomial distribution

    >>> Binomial(5,1,0.1)
    0.9185

    '''
    result=0
    for i in range (0,t+1,1):
        result+=binomial(n,i,p)
    return result



def binomial(n,x,p):
    '''
    (Float,float,float)->float

    Return value of Binomial

    >>>binomial(5,0,0.1)
    0.5905

    '''
    choose=(factorial(n)/(factorial(x)*factorial(n-x)))
    result=(p**x)*((1-p)**(n-x))

    return choose*result


def factorial(n):
    '''
    (int)->int

    Return the factorial of number n

    >>>factorial(5)
    120
    >>>factorial(4)
    24
    
    '''
    if n==1:
        return 1
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def OutputPoisson():
    '''
    ()->table

    Output Poisson Distribution table
    '''
    print 't','\t',' ','0.5',' ',
    for i in range(1,10,1):
        print '%02.1f'%(i),' ',
    for i in range(10,16,1):
        print '%02d'%(i),'  ',    
    print'\n'
    for t in range(0,30,1):
        print t,
        print '\t','%01.3f'%(Poisson(0.5,t)),
        for p in range(1,16,1):
            print '%01.3f'%(Poisson(p,t)),
        print '\n'


def Poisson(p,t):
    '''
    (float,int)->float

    return the value of poisson distribution

    >>>Poisson(3.0,5)
    0.916
    
    '''

    result=0
    for i in range (0,t+1,1):
        result+=poisson(p,i)
    return result
    


def poisson(p,x):
    '''
    (float,int)->float

    Return the value of poisson

    >>>poisson(1,0)
    0.368
    
    '''
    exp=2.718281828349045
    p=p*(1.0)
    choose=exp**(-p)
    result=(p**x)/(factorial(x))
    return choose*result
