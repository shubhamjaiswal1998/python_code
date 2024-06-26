str1="a b c d"
#print(str1.split())#['a', 'b', 'c', 'd']
str2="abcd"
print(str2.split())#['abcd']
str3="a\nb\nc\nd"
print(str3.split())#['a', 'b', 'c', 'd']

l1=['a','b','c','d']
print("".join(l1))#abcd

str4="a b c d"
for i in str4.split():
  print(i,end=" ")     #a b c d

print()
list2=[45,"hello",["abcd","bcd",["apple","banana"]],12]
print(list2)#[45, 'hello', ['abcd', 'bcd', ['apple', 'banana']], 12]
print(list2[0])#45
print(list2[1][0])#h
print(list2[1][1])#e
print(list2[2][0][2])#c
print(list2[2][2][1][2])#n
list2[0]=list2[0]*3
print(list2[0])#135
#list2[1][1]="k" can't do this bocz hello is String that is immutable

"""
Unpacking Tuples:
Tuple unpacking allows you to assign the elements of a tuple to
individual variables. It's a convenient way to extract values from a tuple  """
# Eg: Unpacking a tuple
t = (1, 2, 3)
a, b, c = t
print(a) # Output: 1
print(b) # Output: 2
print(c) # Output: 3
print(t[0])#1

# Eg: Unpacking a tuple with * operator
t = (1, 2, 3, 4,"abcd", 5)
a, *b, c = t
print(a) #  1
print(b) #  [2, 3, 4, 'abcd']
print(c) # 5