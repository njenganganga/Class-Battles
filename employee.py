100#Program to calculate Bonus
salary = float(input("Enter your salary: "))
years =int(input("Enter years of service: "))

if years >10:
    bonus =0.1*salary
    net_salary =bonus +salary
    print("bonus:",bonus)
    print("net salary: ",net_salary)

elif years >=6 and years <=10:
    bonus =0.08*salary
    net_salary =bonus +salary
    print("bonus:",bonus)
    print("net salary: ",net_salary)    

elif years <6:
    bonus =0.05*salary
    net_salary =bonus +salary
    print("bonus:",bonus)
    print("net salary: ",net_salary) 