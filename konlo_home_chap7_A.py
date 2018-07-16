def f2(n):
    # n이 1이면 종료이기 때문에 값을 1로 return 
    if n == 1 :
        return 1

    # even인경우는 integer division으로 하며 호출 수를 더해서 reuturn
    if n % 2 == 0:
        return f2(n//2) + 1
    # odd 인 경우는 3*n + 1로 하고 호출 수 더해서 return 
    else:
        return f2(3*n + 1) + 1

#print(f2(1))
#print(f2(6))
#print(f2(11))
#print(f2(637228127))

def f4(items):

    # list가 없을 때는 return 함 
    if items == [] :
        return

    # 조건이 되면 화면을 출력하고 
    if items[0] % 2 == 1:
        print(items[0] * 3)

    # 재귀함수를 items 하나 줄여서 호출 
    f4(items[1:])
    

#f4([1,2,3,4])
#f4([2,4])
#f4([11,42,63,15])


def f6(items):
    if type(items) != list or items == []:
        return items
    elif type(items[0]) != list:
        return [items[0]] + f6(items[1:])
    else:
        return f6(items[0]) + f6(items[1:])

#print(f6(['baa']))

#print(f6(['baa', [4, True, [10,5], [1,2,['moo']]], ["chirp"]]))
    

def f8(s):

    # 끝가지 온 경우 True return , 홀/짝수일 때 모두 고려 
    if len(s) == 0 or len(s) == 1:
        return True

    #앞 부분 공백 처리
    if s[0] == " ":
        return f8(s[1:])
    #뒷 부분 공백 처리
    if s[len(s)-1] == " ":
        return f8(s[0:len(s)-1])
    #첫자와 앞자가 같으면 다시 나머지 검사 
    if s[0] == s[len(s)-1]:
        return f8(s[1:len(s)-1])
    else:
        return False        

#print(f8(""))
#print(f8("kayak "))
#print(f8("penguin"))
#print(f8("a"))

def f10(list):

    # base list empty 일 경우는 합이기 때문에 0 return 
    if list == [] :
        return 0

    # recursive case : 함수가 얼마나 호출되었는지 확인하면 되기 때문에
    # 호출할 때마다 1를 더해서 return 
    return f10(list[1:]) + 1


#print(f10([1,2,3]))
#print(f10([]))
#print(f10([2]))


def f12(n):

    if n == 0:
        return
    print(n)
    f12(n-1)

    
        
#f12(3)   
#f12(0)
#f12(1)



def f14(items):

    if items == []:
        return None

    # odd 이면 찾았기 때문에 return 하면 됨 
    if items[0] % 2 == 1:
        return items[0]
    # even인 경우는 그 밑에 혹시 있는지 살펴봄
    else:
        return f14(items[1:])


#print(f14([1,2,3]))
#print(f14([2,4]))
#print(f14([2,4,6,8,10,3]))

def f16(items):
    returnValue = []
    if len(items) == 0:
        return []
    
    elif items[0] % 2 == 1:
        returnValue.append(items[0])
        #returnValue.append(f16(items[1:]))

    return returnValue + f16(items[1:])


#print(f16([1,3,5,7]))
#print(f16([2,4]))
#print(f16([1,2,3,4,5]))


# f18은 다시 풀어야함 --------------------------------------
#def f18(a, b):


# merge 
def f19(items1, items2):

    a_index = 0
    b_index = 0
    returnValue = []
    while a_index < len(items1) and b_index < len(items2):
        if items1[a_index] < items2[b_index]:
            returnValue.append(items1[a_index])
            a_index += 1
        else:
            returnValue.append(items2[b_index])
            b_index += 1

    returnValue.extend(items1[a_index:])
    returnValue.extend(items2[b_index:])
    return returnValue

def f20(items):
    if len(items) == 1 or len(items) == 0:
        return items

    
    mid_index = len(items)//2
    head_list = f20(items[0:mid_index])
    tail_list = f20(items[mid_index:])

    return f19(head_list, tail_list)

print(f20([3,2,1,100]))
print(f20([]))    
print(f20([5,3,1,2,4,6]))    

    
