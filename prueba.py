def minTime(machines, goal):
    from decimal import Decimal
    machines.sort()
    sum_mach = sum(1/x for x in machines)
    days = (goal/sum_mach)       
    cont = 1
    print(days)
    while True:
        cont += 1
        if cont == 100: break
        min_mac = min([x - (days % x) for x in machines]) 
        sum_day = sum(days//x for x in machines)
        if sum_day >= goal:
            break              
        else: days += min_mac
        print(sum_day)
    return(int(days)) 

with open("Archivo//datos.txt","r") as dat:
    machines = list(map(int, dat.readline().split()))
    goal = 313369020

print(minTime(machines, goal))

# 340655733624
# 340628671584