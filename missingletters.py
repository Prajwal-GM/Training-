'''Pangram is a sentence containing every letter in the English alphabet. Given a string, 
find all characters that are missing from the string, Le., the characters that can make 
the string a Pangram We need to print output in alphabetic order.
For example,
Input: welcome to geeksforgeeks
Output: abdhijnpquvxyz'''


sen=input().lower()
res=[]
a='abcdefghijklmnopqrstuvwxyz'
for i in a:
    if i not in sen:
        res.append(i)
print("".join(res))
