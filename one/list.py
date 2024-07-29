'''
Write a program to rotate a linked list from left to right by 'k' element.
Input: linked list = 10->20->30->40->50->60, k = 4
Output: 50->60->10->20->30->40.'''
lst=list(map(int,input().split()))
k=int(input("Enter: "))
new_lst=[]
i=k
j=0
while (i<len(lst)):
    new_lst.append(lst[i])
    i+=1
print(new_lst)
while (j<k):
        new_lst.append(lst[j])
        j+= 1
print("Output:  ",new_lst)
