def minTime(machines, goal):
    sum_mach = sum(1/x for x in machines)
    days = [1, int(goal/sum_mach)]      
    n = 1
    print(days[-1])
    while True:               
        sum_prod = sum(days[-1]//x for x in machines)
        prom = ((goal-sum_prod)/2)**n;   
        min_mac = min([x - (days[-1] % x) for x in machines]) * prom
        if sum_prod >= goal:
            if prom == 1:
                break 
            else:
                days[-1] = days[-2]
                n = 0                     
        else: 
            days.append(days[-1]+min_mac)            
        print(prom, sum_prod)        
    return(int(days[-1])) 
    

with open("Archivo//datos.txt","r") as dat:
    machines = list(map(int, dat.readline().split()))
    goal = 313369020

print(minTime(machines, goal))

# 340655733624
# 340628671584