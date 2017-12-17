
t = int(input())

for i in range(t):
    k = int(input())
    depan = (k-1) // 4
    if depan != 0:
        print(depan, end='')

    sisa = k % 4
    if sisa == 1:
        print(192)
    if sisa == 2:
        print(442)
    if sisa == 3:
        print(692)
    if sisa == 0:
        print(942)
