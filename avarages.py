
def sum_num():
    list2=take5_input()
    print(list2)
    sum1=0
    sum2=0
    for i in list2:
        if i>0:
            sum1=sum1+i
        else:
            sum2=sum2+i    
    print("+ve sum is ",sum1)
    print("-ve sum is ",sum2)
    average = (sum1+sum2) / len(list2)
    print("average is ",average)

def take5_input():
    list1=[]
    for i in range(1,6):
        num=int(input("enter number"))
        list1.append(num)
    return list1
sum_num()

#////////////////////////////////////////////////////
def calculate_mean(list1):
    total_sum = sum(list1)
    count = len(list1)
    mean = total_sum / count
    print("mean is ",mean) 
    return mean

list1 = [8, 2, 3, -1, 2]
mean=calculate_mean(list1)
def calculate_variance(list1, mean):
    squared_differences = []
    for x in list1:
        squared_differences.append((x - mean) ** 2)
    variance = sum(squared_differences) / len(list1)
    print("variance is ",variance)#
    print("standard deviation is ",variance**0.5)#
calculate_variance(list1,mean)   

#////////////////////////////////////////////////////////


def bubble(list1):
    n=len(list1)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if list1[j]>list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return list1
print(bubble(["Charlie", "Alice", "Bob", "David", "Eve"]))
           
#///////////////////////////////////////////////////////////
def average(list1):
    try:
        total_sum = sum(list1)
        count = len(list1)
        avg = total_sum / count
    except ZeroDivisionError:
        avg = 0.0
    return avg
print(average([1, 2, 3, 4, 5]))  
print(average([]))  
print(average([10, 20, 30])) 

#A list is an ordered collection of items that is mutable,
#A tuple is an ordered collection of items that is immutable, 
# A set is an unordered collection of unique items that is mutable.
#set
# Define two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# a) intersection()
intersection_set = set_a.intersection(set_b)
print(intersection_set)#{4, 5}

# b) union()
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)#{1, 2, 3, 4, 5, 6, 7, 8}

# c) issubset()
set_c = {1, 2}
is_subset = set_c.issubset(set_a)
print("set_c is subset of set_a:", is_subset)#true

# d) difference()
difference_set1 = set_a.difference(set_b)
difference_set2 = set_b.difference(set_a)
print(difference_set1)#{1, 2, 3}
print(difference_set2)#{8,6,7}

# e) update()
set_d = {9, 10}
set_a.update(set_d)
print("Updated set_a after adding set_d:", set_a)#{1, 2, 3, 4, 5, 9, 10}

# f) discard()
set_a.discard(10)
print("set_a after discarding element 10:", set_a)#{1, 2, 3, 4, 5, 9}


#///////////////////////////////////////////////////////////////
def print_list(list1):
    for i in range(len(list1)-1,-1,-1):
        print(list1[i],end=" ")

print_list([1, 2, 3, 4, 5, 9])

#/////////////////////////////////////////////////////////////
def reverse_list_recursive(lst):
    #  if the list is empty or has one
    if len(lst) <= 1:
        return lst
    first_element = lst[0]
    rem_list = lst[1:]
    reversed_list =reverse_list_recursive(rem_list)
    r=reversed_list+[first_element]
    return r
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list_recursive(my_list)
print("Original list:", my_list)
print("Reversed list:", reversed_list)
print([1,2]+[3,4])#[1,2,3,4]


#////////////////////////////////////////////////////////////
def exchange_first_last(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]
print(exchange_first_last("abcd"))

    
# Using a lambda function /////////////////////
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
num = [1, 2, 3, 4]
even=list(filter(lambda n:n%2==0,num))
add_5=list(map(lambda n:n+5,even))
squared = map(lambda x: x**2, num)
print(list(squared))  # Output: [1, 4, 9, 16]
print(even)
print(add_5)

