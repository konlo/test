def f2(list):

    for value in list:
        if value % 2 == 1:
            print(value)



#f2([1,2,3,4])
#f2([1,2,3,4,5])


def f4(list):
    sum = 0 
    for index in range(0, len(list)):
        if list[index] % 2 == 1:
            sum = sum + index
    return sum

#print(f4([1,2,3,4]))
#print(f4([1,2,3,4,5]))


def f8(a,b,n):

    for value in range(a, b+1):
        if value % n == 0:
            print(value)

#f8(1,10,2)
#print("--")
#f8(1,10,11)
#print("--")
#f8(1,10,7)

def f10(n):

    for value in range(n):
        print("*" * (value+1) )

#f10(1)
#f10(2)
#f10(10)

def f12(list):

    if len(list) == 0 : return True
    
    for value in list:
        if value >= 0 :
            return False

    return True
        

#print(f12([]))
#print(f12([-1,-2,-3,-4,5]))
#print(f12([1,2,3,4,5]))
#print(f12([-1,-2,-3]))


def f14(list):
    lastIndex = 0

    for n in range(0, len(list)):
        if list[n] < 0:
            lastIndex = n
            
    return lastIndex

#print(f14([1,2,-3]))
#print(f14([1,-2,-3, 1, -2, -3]))
#print(f14([-1,1,1,1]))


def f16(n):

    for n in range(n,0, -1):
        print("*" * n)

#f16(3)
#f16(2)
#f16(1)

def f18(n):
    nResult = 1

    for nValue in range(n,0,-1):
        nResult = nResult * nValue
    return nResult

#print(f18(0))
#print(f18(2))
#print(f18(3))


def f20(list):

    for nValue in list:
        for Count in range(nValue, -1, -1):
            print(Count, end=" ")
        print()

#f20([])
#f20([1,3,5])
#f20([5,3,6,2])

def f22(n):

    for nValue in range(1, n+1):
        if nValue % 2 == 0 or nValue % 3 == 0:
            print(nValue)


#f22(10)
#f22(1)
#f22(3)
    

def f24(list):

    # 적어도 두개는 입력이 들어온다고 했으니
    # 처음 두 수를 비교해서 first second를 구별해서 넣는다. 
    if(list[0] > list[1]):
       nFirst = list[0]
       nSecond = list[1]
    else:
       nFirst = list[1]
       nSecond = list[0]       
    

           
    # 수를 비교 하고 더 큰 값이 나오면 더 현재 큰 값은 second
    # 새로운 큰 것은 first에 넣어준다. 
    for nValue in list:
        if nValue > nFirst:
            nSecond = nFirst
            nFirst = nValue

    return nSecond

#print(f24([1,4,3,2,5]))
#print(f24([3,2]))
#print(f24([3,4]))

def f26(items):
    for row in items:
        #첫번째 값을 넣는다. 
        MaxValue = row[0]
        for value in row:
            if MaxValue < value:
                MaxValue = value
        print(MaxValue)            
        
f26([[1 ,2,3],[4,5,6],[7.8,9]])
f26([[3,2,1],[0,-1 ,-21]])
f26([[1,2,3,4],[1],[34],[2],[3],[56],[67]])    
