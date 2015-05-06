'''
Created By Felice Lin in May 6th 2015

For Probability & Statistics Python assignment

Choose four days for holiday in June 2015

Rules:
1. No consecutive for holiday.
2. No more than two days holiday on weekends.
3. Cannot have holiday on Lunar 1st or 15th.

'''
import math

def fac(n):
    '''
    (int)->int

    Return the factorial of number n

    >>>fac(5)
    120
    >>>fac(4)
    24
    
    '''
    if n==1:
        return 1
    if n==0:
        return 1
    else:
        return n*fac(n-1)

def Holiday(n):
    '''
    >>>Holiday(2)
    24
    '''
    return C(4,n)*(C(2,1)**n)


def C(a,b):
    '''
    >>>C(4,2)
    6
    '''
    return fac(a)/(fac(a-b)*fac(b))

def choose():
    '''
    '''
    weekend=[6,7,13,14,20,21,26,27]
    lunar=[1,16,30]
    June=[i for i in range(1,30+1)]
    days=(set(June)-set(weekend)-set(lunar))
    count=0
    Days=list(days)
    
    #two days on weekends
    for first in weekend:
        for second in weekend[weekend.index(first)+1:]:
            if first+1!=second:
                for i in Days:
                    for j in Days[Days.index(i)+1:]:
                        if i+1!=j:
                            if i not in [first+1,first-1,second+1,second-1]:
                                if j not in [first+1,first-1,second+1,second-1]:
                                    print(first,second,i,j)
                                    count+=1

    #one day on weekends
    for first in weekend:
        for i in Days:
            for j in Days[Days.index(i)+1:]:
                for k in Days[Days.index(j)+1:]:
                    if i+1!=j and j+1!=k:
                        if i not in [first+1,first-1]:
                            if j not in [first+1,first-1]:
                                if k not in [first+1,first-1]:
                                    print(first,i,j,k)
                                    count+=1

    #none any day on weekends
    for i in Days:
        for j in Days[Days.index(i)+1:]:
            for k in Days[Days.index(j)+1:]:
                for m in Days[Days.index(k)+1:]:
                    if i+1!=j and j+1!=k and k+1!=m:
                        print(i,j,k,m)
                        count+=1

    print(count)
















