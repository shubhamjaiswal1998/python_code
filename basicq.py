def revere(s):
    s1=""
    i=len(s)-1
    while i>=0:
        r=s[i]
        s1=s1+r
        i=i-1
    return s1
#print(revere("abcd")) 
#///////////////////////////////////////////////////
l1=[1,2,3,4]
d=dict(enumerate(l1))
print(d)

#/////////////////////////////////////////////////////
'''yuvycuvdsyuvyudvcyusdvcyusdvyd'''

def check_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(check_prime(6))
#///////////////////////////////////////////////////////////////
def print_prime(a,b):
    for i in range(a,b+1):
        r=check_prime(i)
        if r:
            print(i,end=" ")
print_prime(5,36)
#/////////////////////////////////////////////////////////////////////////////
def hcf(a,b):
    m=min(a,b)
    i=2
    gcd=1
    while i<=m:
        if a%i==0 and b%i==0:
            gcd=i
        i=i+1
    return gcd 
print()
print("hcf is ",hcf(15,24))
#///////////////////////////////////////////////////////////////////////////////////
def lcm(a,b):
    i=1
    while i<=b:
        f=a*i
        if f%a==0 and f%b==0:
            return f
        i=i+1
print("lcm is ",lcm(10,72))
#////////////////////////////////////////////////////////////////////////////////////////
def sum_digit(n):
    s=0
    while n!=0:
        s=s+n%10
        n=n//10
    return s  
print("sum of digit ",sum_digit(1234)) 
#////////////////////////////////////////////////////////////////////////////////////
def fibo(n):
    print("fibonacci series is ")
    a=0
    b=1
    print(a,end=" ")
    for i in range(0,n):
        print(b,end=" ")
        c=a+b
        a=b
        b=c
fibo(18)

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
print(result)

def combine_list(l1,l2):
    new_list=[]
    for i in range(0,len(l1)):
            new_list.append((l1[i],l2[i]))
    return new_list        
print(combine_list([1,2,3],[4,5,6]))


def divisor(n):
   l1=[]
   for i in range(1,n+1):
        if n%i==0:
           l1.append(i)
   return l1  
print(divisor(18)) 
#///////////////////////////////////////////////////////////////////////////////////
def armstrong(n):
    n1=n
    sum=0
    while n!= 0:
        digit = n % 10
        sum =sum+ digit ** 3
        n =n// 10
    if n1==sum:
        print("yes")
    else:
        print("no") 
armstrong(407) 

'''print(armstrong(407))
print(armstrong(153))
print(armstrong(123))'''

def count_letters(s):
    d=0
    u=0
    l=0
    for i in range(0,len(s)):
        ch=s[i]
        if ch.isdigit():
            d=d+1
        elif ch.isupper():
            u=u+1
        elif ch.islower():
            l=l+1 
    print(d," ",u," ",l) 
count_letters("ABCHJabc1237")      

#///////////////////////////////////////////////////////////////////////////
def selection_sort(arr):
    n = len(arr)
    for i in range(0,n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
#////////////////////////////////////////////////////////////////////////////////////////
def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
arr1=[3,4,5,1,6] 
bubble_sort(arr1)  
print(arr1)   

#/////////////////////////////////////////////////////////////////////////////////////////
data={
    'n1':[1,2,3,4],
    5:["abc","bbc","cbc"],
   
     'n3':[[7,8],[5,9],[0,1]],
     "n4":{4,5,6},
     "n5":[{ "subject":"math",
            "name":"shubham",
            "class":"11th"
         
            },
            { "subject":"english",
            "name":"ankit",
            "class":[99,"abc"]
            }   
            ]

}
print(data["n5"][1]["class"][1]," ",data["n5"][0]["name"])#abc shubahm
print(data[5])#["abc","bbc","cbc"]
print(data[5][1])#bbc


