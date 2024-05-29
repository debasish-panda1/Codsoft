def add():
    x=int(input("enter the first number"))
    y=int(input("enter the second number"))
    print("The result is:")
    print(x+y)
def mul():
    x=int(input("enter the first number"))
    y=int(input("enter the second number"))
    print("The result is:")
    print(x*y)
def sub():
    x=int(input("enter the first number"))
    y=int(input("enter the second number"))
    print("The result is:")
    print(x-y)
def div():
    x=float(input("enter the first number"))
    y=float(input("enter the second number"))
    print("The result is:")
    print(x/y)
print("__CALCULATOR__")
print("1. additon")
print("2. substraction")
print("3. multiplication")
print("4. substraction")
while True:
    choice = int(input("enter your choice for calculation:"))
    if choice == 1:
        add()
        break
    elif choice == 2:
        sub()
        break
    elif choice == 3:
        mul()
        break
    elif choice == 4:
        div()
        break
    else:
        print("invaild choice,retry!!")
    
    