'''

b0229018_calander.py
寫一個程式計算出2015.6有四天休假可以排
1.休假日不可連續
2.最多只能2天在周末(星期六、星期日)
3.農曆的「初一」及「十五」公司要拜拜，不能排休假
求多少種,並列出所有組合

2015/5/6

'''


def main():
    calander()

def calander():
    '''
        ()->(number)
        計算出4月總共有幾種排假方式
    '''
    day=[i for i in range(1,31)]   #set才能相減 tuple,list都不能相減
    weekend=[6,7,13,14,20,21,27,28]
    byebye=[1,16,30]
    realPossible=list(set(day)-set(weekend)-set(byebye))    #除去周末納入考量的日子
    print(realPossible)

    L=[]
    count=0
    #周末兩天
    for item1 in weekend:
        for item2 in weekend[weekend.index(item1)+1:]:
            if item2!=item1+1: #兩天假日不可相鄰
                for item3 in realPossible:
                    if item3 not in [item1-1,item1+1,item2-1,item2+1]: #不可相連
                        for item4 in realPossible[realPossible.index(item3)+1:]:
                            if item4 not in [item1-1,item1+1,item2-1,item2+1,item3-1,item3+1]: #不可相連
                                count=count+1
                                L=[item1,item2,item3,item4]
                                print(L)

 
    #周末一天
    for item1 in weekend:
        for item2 in realPossible:
            if item2 not in [item1-1,item1+1]: #不可相連
                for item3 in realPossible[realPossible.index(item2)+1:]:
                    if item3 not in [item1-1,item1+1,item2-1,item2+1]: #不可相連
                        for item4 in realPossible[realPossible.index(item3)+1:]:
                            if item4 not in [item1-1,item1+1,item2-1,item2+1,item3-1,item3+1]: #不可相連
                                count=count+1
                                L=[item1,item2,item3,item4]
                                print(L)

    #周末零天
    for item1 in realPossible:
        for item2 in realPossible[realPossible.index(item1)+1:]:
            if item2 not in [item1-1,item1+1]: #不可相連
                for item3 in realPossible[realPossible.index(item2)+1:]:
                    if item3 not in [item1-1,item1+1,item2-1,item2+1]: #不可相連
                        for item4 in realPossible[realPossible.index(item3)+1:]:
                            if item4 not in [item1-1,item1+1,item2-1,item2+1,item3-1,item3+1]: #不可相連
                                count=count+1
                                L=[item1,item2,item3,item4]
                                print(L)
    print(count)
    
    
if __name__=='__main__':
    main()
