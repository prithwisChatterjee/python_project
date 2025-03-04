print("Missing Number in sequence and multiple occurance  ")
inPutArray = [2,4,5,1,2,3,6,8]
multiAppear = 0
mismatch = 0
arrLength = len(inPutArray)

for x in range(arrLength):
    for val in inPutArray:           
        if val == x:
            mismatch = x   
            multiAppear = multiAppear+1
        
    if x!= mismatch:  
        print("Missing ")          
        print(x)
    if multiAppear>1:
        print("appears multiple time")
        print(multiAppear)
    multiAppear = 0