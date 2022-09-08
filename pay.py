def pay(h_rate,h_worked):
    if h_worked>40:
        return 1.5*h_worked*h_rate
    else:
        return h_worked*h_rate
        
w=int(input("Enter the hours worked : "))
r=int(input("Enter the hour rate : "))
print("Total payment is "+str(pay(r,w)))
