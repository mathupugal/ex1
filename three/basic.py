'''
Question 2: Basic Mathematics

Problem Statement:
Print all those elements that have no element greater than them in the right side of the array. Print elements from right to left.

Example:
```python
Input : A[] = [1, 2, 3, 4, 5]
Output : 5
Explanation : Only 5 has no element greater than it on its right.

Input : A[] = [1, 4, 3, 2]
Output : 2 3 4
Explanation : 2, 3, and 4 have no elements greater than them on their right while 1 has 4, 3 and 2 greater than it on its right.'''

a=list(map(int,input("Enter:" ).split()))
new_lst=[]
for i in range(len(a)):
  for j in range(i+1, len(a)):
    if a[i]>=a[j]:#condition true means break
      continue
    else:
      break
  else:
        new_lst.append(a[i])

print(new_lst)
new_lst.sort()
print("Output:", new_lst)

