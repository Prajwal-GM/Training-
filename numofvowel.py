def max_vowel_count(s):
    s = s.lower()
    vowels = 'aeiou'
    vowel_count={}
    for vowel in vowels:
        vowel_count[vowel]=s.count(vowel)
        max_vowel = max(vowel_count,key=vowel_count.get)
        return max_vowel
print(max_vowel_count("happy fathers day"))