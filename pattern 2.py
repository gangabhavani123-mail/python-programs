for i in range(5):
    for j in range(i + 1):
        print('*', end='')
    print()
s={1,4,10,25,67}
for num in s:
    print((num,hash(num)%len(s)))
    print(s)
