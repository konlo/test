def f2(n):
    nPrintValue = 1
    for PrintCount in range(n):
        for i in range(0, PrintCount+1):
            print(nPrintValue, end = " ")
            nPrintValue += 1

        print()
#f2(3)
#f2(0)
#f2(5)

def f4(n):
    nPrintValue = 1
    for PrintCount in range(n):
        for i in range(0, PrintCount+1):
            print(nPrintValue, end = " ")
            nPrintValue += 1

        print()
        
    for PrintCount in range(n-1,0,-1):
        for i in range(0, PrintCount):
            print(nPrintValue, end = " ")
            nPrintValue += 1

        print()

#f4(3)

def f6(maxtrix):
    for i in range(len(maxtrix[0])):
        print(maxtrix[i][i])

#f6([[1,0],[0,1]])
#f6([[1,2,3],[4,5,6],[7,8,9]])
#f6([[1]])
def f8(matrix):

    sum = 0 
    for row in matrix:        
        for value in row:
            sum += value
        
    return sum

#print(f8([[1,0],[0,1]]))
#print(f8([[1,2,3],[4,5,6]]))
#print(f8([[1],[2],[3],[4]]))

def f10(matrix):
    for row in matrix:
        for value in row:
            if value % 2 == 1:
                print(value, end = " ")
        print()

#f10([[1,0],[0,1]])
#f10([[1,2,3],[4,5,6]])
#f10([[1],[2],[3],[4]])

def f12(matrix1, matrix2):
    result_row_len = len(matrix1)
    result_column_len = len(matrix2[0])
    sum_len = len(matrix2)
    

    resultValue = []

    for i in range(result_row_len):
        rows = []    
        for j in range(result_column_len):
            rows.append(0)

        resultValue.append(rows)
    
        
    #print("{0} x {1}, {2} ".format(result_row_len,result_column_len, sum_len))
    for i in range(result_row_len):
        
        for  j in range(result_column_len):
            total_sum = 0
            for k in range(sum_len):
                # column 수만큼 합이 발생함
                
                sum = matrix1[i][k] * matrix2[k][j]
                total_sum += sum

            resultValue[i][j] = total_sum

    print(resultValue)

f12([[1,0],[0,1]],[[1,0],[0,1]])
f12([[1,2,3],[4,5,6]],[[-1,-1],[-1,-1],[-1,-1]])
f12([[4,3,2,1]],[[1],[2],[3],[4]])

def f14(rows, cols):

    returnValue = []
    for row in range(rows):
        adjact_value = []
        for col in range(cols):
            adjacent_count = 0
            
            #check above
            if row - 1 >= 0 :
                adjacent_count += 1              
            
            #check below 
            if row + 1 < rows :
                adjacent_count += 1              
                
            #check left
            if col - 1 >= 0:
                adjacent_count += 1
            
            #check right
            if col + 1 < cols :
                adjacent_count += 1
            adjact_value.append(adjacent_count)

        returnValue.append(adjact_value)

    return returnValue

            
                
    
            
#print(f14(3,3))
