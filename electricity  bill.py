#electricity bill
def bill():
    customerID = float(input("Enter your customerID: "))
    customerNAME = float(input("Enter your customerNAME: "))
    Unitsconsumed = float(input("Enter the Unitsconsumed: "))
    
    if Unitsconsumed >=0 and Unitsconsumed <=199:
     bill=Unitsconsumed*1.20
     print("Your Bill is: ", bill)

    elif Unitsconsumed>=200 and Unitsconsumed <=400:
     bill=Unitsconsumed*1.50
     print("Your Bill is: ", bill)

    elif Unitsconsumed>=400 and Unitsconsumed <=600:
     bill=Unitsconsumed*1.80
     print("Your Bill is: ", bill)

    elif Unitsconsumed>600:
     bill=Unitsconsumed*2.00
     print("Your Bill is: ", bill)    

    else:
     print("Invalid input!!")    

def kplc(customerID, customerNAME, Unitsconsumed):
  if Unitsconsumed>=1999:
    charge = 1.2*Unitsconsumed
  elif Unitsconsumed>=200 and Unitsconsumed < 400:
    charge = Unitsconsumed*1.5
  elif Unitsconsumed <=400 and Unitsconsumed <600:
    charge = Unitsconsumed*1.8
  elif Unitsconsumed >600:
    charge = Unitsconsumed*2.00
    return charge

customerID = int(input("Enter Id"))
customerNAME = input("Enter your name") 
Unitsconsumed = int(input("Enter units"))
 
    
