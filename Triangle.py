h = int(input("Number: "))
w = 2 * (h - 1) + 1
c = w // 2

for i in range(h):
    print(i, end='\t')
    for j in range(w):
        if j == c - i or j == c + i or i == h - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()

for i in range(h):
    print(i, end='\t')
    for j in range(w):
        if j >= (c - i) and j <= (c + i) or i == h - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()

for i in range(h):
    print(i, end='\t')
    for j in range(w):
        if j >= (c - i) and j <= (c + i) or i == h - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
for i in range(h - 1):
    print(i, end='\t')
    for j in range(w):
        if j == c - (h-2 - i) or j == c + (h-2 - i):
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()

for i in range(h):
    print(i, end='\t')
    for j in range(w):
        if j >= (c - i) and j <= (c + i) or i == h - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
for i in range(h - 1):
    print(i, end='\t')
    for j in range(w):
        if j == c or j == c - (h-2 - i) or j == c + (h-2 - i):
            print('* ', end='')
        else:
            print('  ', end='')
    print()