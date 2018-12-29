#Queen positioning method
def n_queen(row,column,n):
    while(column<n):
        if is_attack(row,column,n)==True:
            column+=1
        else:
            temp_list.append([row,column])
            if(row==n-1):
                return True
            else:
                rec = n_queen(row+1,0,n)
                if(rec == True):
                    return True
                else:
                    temp_list.pop()
                    column+=1
    return False

#If queen is under attack method
def is_attack(row,column,n):
    for i in temp_list:
        a,b=i[0],i[1]
        
        #Checking rows and column
        if(row==a and column==b):
            return True
        
        #Checking left down diagonal
        a,b=i[0],i[1]
        while (a>=0 and b>=0 and a<n and b<n):
            if(row==a and column==b):
                return True
            a+=1
            b-=1
        
        #Checking right down diagonal
        a,b=i[0],i[1]
        while (a>=0 and b>=0 and a<n and b<n):
            if(row==a and column==b):
                return True
            a+=1
            b+=1
            
        #Checking left up diagonal
        a,b=i[0],i[1]
        while (a>=0 and b>=0 and a<n and b<n):
            if(row==a and column==b):
                return True
            a-=1
            b+=1
        
        #Checking right up diagonal
        a,b=i[0],i[1]
        while (a>=0 and b>=0 and a<n and b<n):
            if(row==a and column==b):
                return True
            a-=1
            b-=1
    return False


temp_list = []
n=int(input("Enter the value of n in which n is the nxn matrix of chessboard: "))
possible = n_queen(0,0,n)
if(possible == True):
    print("It is possible to put ",n," queens in ",n," x ",n," chessboard")
    print(temp_list)
else:
    print("Whoops! It is not possible to put ",n," queens in ",n," x ",n," chessboard")
