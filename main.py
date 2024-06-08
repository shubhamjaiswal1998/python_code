import calculater
def calculate():
    n1=int(input("enter 1st number"))
    n2=int(input("enter 2nd number"))
    print("choice 1/2/3/4")
    choice=int(input("enter choice"))
    if choice==1:
        print(f"sum is {n1+n2}")
    elif choice==2:
        print(f"subtraction is {n1-n2}")
    elif choice==3:
        print(f"product is {n1*n2}")
    elif choice==4:
        print(f" adfter division result {n1+n2}")
    else:
        print("select right choice")   
calculate()         
    
    
    
