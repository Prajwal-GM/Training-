arr= input()
vowel=['a','e','i','o','u']
count=0
for i in arr:
    if i in vowel:
        count+=1
print(count)