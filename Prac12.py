#a='1121231234'
a='0010120123'
b='**********'
c='AAAAAAAAAA'
print(b[0])
print(b[1:3])
print(b[3:6])
print(b[6:10])

print(a[0])
print(a[1:3])
print(a[3:6])
print(a[6:10])

print(c[0])
print(c[1:3])
print(c[3:6])
print(c[6:10])


n=5;
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

'''numlist =  list()
while True:
    inp = input('')
    if inp=='done':
        break
    numlist.append(inp)
    print(numlist)'''