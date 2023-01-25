b = int(input("Input number of days "))

if b > 0:
    print(b)
else:
    b = int(input("Days must be positive "))


print("Day 1:","1")
days = 1
aIncrement = 2 
penny = 1



for i in range(b):
    m = 1000000
    pAmount = int(penny*2) 
    addAmount = int(2**aIncrement -1) 
    aIncrement +=1
    days +=1
    penny *= 2 
    
    if pAmount > m:
        print("Now you are millionaire")
        
    
    print("Day " + str(days) + ":",pAmount)
