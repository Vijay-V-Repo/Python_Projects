word=list(input())
vowels=[]
for i in range(len(word)):
    if word[i] in 'aeiou':
        vowels.append(i)
c=word[::-1]  
vowels.sort(reverse=True)
for i in range(len(vowels)):
   c.pop(vowels[i])
print(''.join(c))