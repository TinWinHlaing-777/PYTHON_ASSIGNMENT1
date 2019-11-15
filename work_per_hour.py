hour=int(input("Enter the working hour: "))
cost=int(input("Enter the cost for one hour: "))
total=int(hour*cost)
if(hour>40):
    total*=2

print(total)