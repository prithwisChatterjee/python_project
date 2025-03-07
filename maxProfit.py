# Problem:Stock Buy and Sell – Max one Transaction Allowed
# Given an array prices[] of length N, representing the prices of the stocks on different days, the task is
# to find the maximum profit possible by buying and selling the stocks on different days when at most one 
# transaction is allowed. Here one transaction means 1 buy + 1 Sell.
# This Algo provides the earliest buy day and earliest Sell day.If same profit can be made later and on minimum
# days this algo does not check that condition.


price = [10,2,1,3,9,6,8,4,1]
length = len(price)
maxPRofit = 0
buyday = 0
sellDay = 0
for x in range(length):    
    for y in range(x+1,length):
        if (price[y]-price[x])>maxPRofit:
            maxPRofit=price[y]-price[x]
            buyday=x
            sellDay=y

print("buyday on day")           
print(buyday+1)    

print("Sell on day")           
print(sellDay+1)               