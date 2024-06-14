list1=[[1,1],[1,1]]
list2=[[1,1],[1,1]]
#output[[2,2],[2,2]]
def add(list1,list2):
    list3=[]
    for i in range(0,len(list1)):
        list4=[]
        for j in range(0,len(list2)):
            list4.append(list1[i][j]+list2[i][j])
        list3.append(list4)
    return list3
print(add(list1,list2))   

def add1(list1,list2):
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            list1[i][j]=list1[i][j]+list2[i][j]
    return list1        

print(add1(list1,list2)) 
            



