'''
30) Boring Arrays
You are given an array A of size N. In one operation you can select any two elements
from it, add their absolute difference in your score.
Your task is to find and return an integer value, representing the maximum score.
Note:
Assume 1 based indexing
The elements on which operation has been performed cannot be selected again.
Input Specification:
Input1: An integer value N, representing the size of array A
input2: An integer array A
Output Specification:
Return an integer value, representing the maximum score
Sample Input:
4
1 2 3 4
Sample Output:
4
'''

n=int(input())
arr=list(map(int,input().split()))
start=0
end=-1
score=[]
while(len(arr)>1):
    score.append(abs(arr[start]-arr[end]))
    arr.pop(start)
    arr.pop(end)
print(sum(score))
