# Basic Calculator in python
# Function to add two numbers 
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        return "Error! Division by zero not allowed."
    else:
        return x/y
    
def calculator():
    print("Select Operation:")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")

    while True:
        choice = input("Enter Choices (1/2/3/4) :")
        # check if the input is one of the four options
        if choice in ['1','2','3','4']:
            n1 = float(input("Enter the First Number : "))
            n2 = float(input("Enter the Second Number : "))
            if choice == '1':
                print(f"{n1} + {n2} = {add(n1,n2)}")
            if choice == '2':
                print(f"{n1} - {n2} = {sub(n1,n2)}")
            if choice == '3':
                print(f"{n1} x {n2} = {mul(n1,n2)}")
            if choice == '4':
                print(f"{n1} / {n2} = {div(n1,n2)}")

        # option to exit the loop
        next_calculation = input("Do you want to perform another calculation ?")
        if next_calculation.lower() != "yes":
            break
    print("Exiting Calculator, Goodbye!")

# call the function 
calculator()
