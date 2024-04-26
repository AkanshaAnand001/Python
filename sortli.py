l1=[11,24,56]
l2=[4,5,9,67]

'''l3=l1+l2
print (l3)'''

##or

l1.sort()
l2.sort()
s1=len(l1)
s2=len(l2)
l3=[]
#int (i,j)
while i<s1 and j<s2:
    if l1[i] < l2[j]:
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[j])
        j+=1
print(l3)



