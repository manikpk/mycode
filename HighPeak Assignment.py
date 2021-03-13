def findMinimumDifference():
    
    startIndex=0
    endIndex=0
    result = +2147483647  
    # Sorting the array. 
    arr.sort() 
    #print(arr)
    # Find minimum value among 
    # all K size subarray. 

    for i in range(n-k+1):
        oldValue = result
        result = int(min(result, arr[i+k-1] - arr[i])) #Calculates the minimum difference
        if(oldValue != result): 
            startIndex = i
            endIndex = i+k-1


    outputArray=[]
    for i in range(startIndex,endIndex+1):
        outputArray.append(arr[i])
    #print(disparr)
    f.write("The goodies selected for distribution are:\n\n\n")
    for i in range(len(outputArray)):
        outputString = str(dict[outputArray[i]]+": "+str(outputArray[i])+"\n") #Displays the final output in the form of string so that it can be written into the file.
        f.write(outputString) #Writing output into the file
    extra = str("\n\n\nAnd the difference between the chosen goodie with highest price and the lowest price is: "+str(result)+"\n")
    f.write(extra)
    f.close()


# Driver code 
k=int(input("Enter the Number of Employees:"))
f = open("output.txt","a") #Opens the output file
with open('input.txt','r') as file:  #Opens the input file in read mode
    string = file.read()

array1 = list(string.split("\n")) #Splits the newline character of the data from input file
arr=[]
dict={}
for i in array1:
    (key,val)=i.split(": ") #Splits the items and their prices into the dictionary from input file
    dict[int(val)] = key  #Key is Price and its value is the name of the item
    arr.append(int(val))
#dup_value=arr  
#print(dict)
n =len(arr)
findMinimumDifference() #Function call
