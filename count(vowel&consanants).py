s="studying"
vowel_count=0
consanants_count=0
for char in s:
    if char in "aeiou":
        vowel_count+=1
    else:
        consanants_count+=1
print("vowel",vowel_count)
print("consanants",consanants_count)
        
