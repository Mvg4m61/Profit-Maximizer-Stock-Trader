def stock():
    l1 = []
    n = int(input("\nEnter number of days: "))
    for i in range(n):
        num = int(input("Enter respective stock value for the day: "))
        l1.append(num)
    j = 0
    l1.append(0)
    buy = l1[0]
    sell = l1[1]
    sellday = 2
    buyday = 1
    flag = 0
    for i in range(1,n+1):
        if l1[i]>=l1[i-1]:
            sell = l1[i]
            sellday = i+1
        else:
            if (buyday==sellday-1) and flag==0:
                buyday+=1
                sellday+=1
                continue
            print("\nBuy on day ",buyday," for ",buy)
            print("\nSell on day ",sellday," for ",sell)
            print("\nProfit: ",sell-buy)
            flag = 1
            buyday = i+1
            buy = l1[i]
    if flag==0:
        print("\nNo profit.")
           
stock()