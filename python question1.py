
# 1.use if else
age=int(input("enter age"))
if age >= 13 and age <= 19:
 print("You are a teenager")
else:
 print("You are not a teenager")
  

 #2. make authintication system
 fix_username = "admin"
fix_password = "password123"
# Get the user's input for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")
# Check if the entered username and password match the correct ones
if username ==  fix_username and password == fix_password:
 print("Access granted.")
else:
 print("Access denied.")

#3. assignment oprater 
x=25
x+=25
x-=25
x*=5
x//=5 
x%=24
print(x)

#4. make calculater
num1=float(input("enter first number"))
num2=float(input("enter second number"))
choice= input("enter your choice")
if choice=='1':
    result=num1+num2
    print("result is ",result)
elif choice=='2': 
    result=num1-num2 
    print("result is ",result) 
elif choice=='3': 
    result=num1*num2
    print("result is ",result)  
elif choice=='4': 
    result=num1/num2  
    print("result is ",result) 
elif choice=='5': 
    result=num1%num2   
    print("result is ",result)

#5. convert celsius to fahrenheit
choice=input("enter your choice")
if choice == '1':
    C = float(input("Enter temperature in Celsius (C): "))
    F = (C * 9/5) + 32
    print("result is ",F,"Fahrenheit")
elif choice == '2':
    F = float(input("Enter temperature in Fahrenheit (F): "))
    C = (F - 32) * 5/9
    print("result is ",C,"Celsius")
else:
    print("Invalid input. Please choose a valid option (1/2).")
    
#6. get discount 10% at any price if age is grater than 65
price = float(input("Enter the price of the item: Rs"))
# Get the user's age
age = int(input("Enter your age: "))
# Check if the user is 65 or older and apply the discount if applicable
if age >= 65:
    discount = 0.1  # 10% discount for users 65 or older
else:
    discount = 0.0  # No discount for users younger than 65

final_price=price-(discount*price)   
print (f"Final price after applying discount: {final_price}") 

#7. check password weakness
password = input("Enter a password: ")
password_length = len(password)
if password_length < 8:
     print("The password is Weak")
elif 8 <= password_length and password_length <= 12:
       print("The password is mediam ")
else:
      print("The password is Strong")


#8. calculate gcd
num1=9
num2=3
while num2!=0: # when num2 is 0 at that time return num1
    num1=num1%num2 #first divide number then swap num1 & num2
    temp=num1
    num1=num2
    num2=temp
print("hcf is ",num1)    








