lis=[(2,5),(1,2),(4,4),(2,3,),(2,1)]
length=len(lis)
for i in range(0,length):
    for j in range(0, length-i-1):
        if (lis[j][1]>lis[j+1][1]):
            temp=lis[j]
            lis[j]=lis[j+1]  #We are doing swaping if condition is true.
            lis[j+1]=temp            
print("In increasing order:", lis)            
