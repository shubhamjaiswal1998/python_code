def mul(l1,l2):
    r1=[]
    for i in range(0,len(l1)):
        row=[]
        for j in range(0,len(l2)):
            res=0
            for k in range(0,len(l1)):
                res=res+l1[i][k]*l2[k][j]
            row.append(res)
        r1.append(row)
    return r1  
list1=[[1, 2],[3, 4]]  
list2=[[5, 6],[7, 8]]
print(mul(list1,list2))#[[19, 22], [43, 50]]
print(mul([[1,1],[1,1]],[[1,1],[1,1]]))

#///////////////////////////////////////////////////////////////
def transpose(list1):
    r=[]
    for i in range(0,len(list1)):
        r2=[]
        for j in range(0,len(list1)):
            r2.append(list1[j][i])
        r.append(r2)     
    return r
print(transpose([[1, 2],[3, 4]]))#[[1, 3], [2, 4]]

#////////////////////////////////////////////////////////////
def add(l1,l2):
    r1=[]
    #r2=[]
    for i in range(0,len(l1)):
        r2=[]
        for j in range(0,len(l2)):
            r2.append(l1[i][j]+l2[i][j])
        r1.append(r2)
    return r1    
result=add([[1,1],[1,1]],[[1,1],[1,1]])    
print("after adding 2dlist is ")
print(result)#[[2, 2], [2, 2]]
