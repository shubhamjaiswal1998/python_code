def sum_of_10_num():
    sum =0
    for i in range(1,11):
        sum=sum+i
    print(sum)
sum_of_10_num()        
#///////////////////////////////////////////////////

def even_sum(n):
    even_sum=0
    for i in range(1,n+1):
        if i%2==0:
            even_sum=even_sum+i
    print(even_sum)  
even_sum(6)
#//////////////////////////////////////////////////

def swap(a,b):
    t=a
    a=b
    b=t
    print("1st ele ",a)
    print("2nd ele ",b)  
swap(2,3)    
#/////////////////////////////////////////////////////

def swap1(a,b):
    a=a+b
    b=a-b
    a=a-b
    print("1st ele ",a)
    print("2nd ele ",b)
swap1(2,3)    

def greatest(a,b,c):
    if a>b and a>c:
        print("greatest number is ",a)
    elif b>a and b>c:
        print("greatest number is ",b)
    else:
        print("greatest number is ",c)
greatest(2,3,5)      

#////////////////////////////////////////////////////////////////
def max_2_num(a,b):
    if a>b:
        print("greatest number is ",a)
    else:
        print("greatest number is ",b)   
max_2_num(89,60)  

def palindrome_num(n):
    num1=n
    sum=0
    while n!=0:
        r=n%10
        sum=sum*10+r
        n=n//10
    if sum==num1:
        print("palindrome")
    else:
        print("not palindrome ") 
palindrome_num(1221)   

def palindrome1(str1):
    str3=str1
    new_str=""
    length=len(str1)-1
    while length>=0:
        new_str=new_str+str1[length]
        length=length-1
    if str3==new_str:
        print("palindrome")
    else:
        print("not palindrome ") 
palindrome1("abbaa")  

#print calender
import calendar
def print_month_calendar(year, month):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar(calendar.SUNDAY)
    # Print the calendar for the specified month and year
    month_calendar = cal.formatmonth(year, month)
    print(cal)#<calendar.TextCalendar object at 0x000002917E127380>
    print(month_calendar)#actual calender
year = 2024
month = 6
print_month_calendar(year, month)


        
