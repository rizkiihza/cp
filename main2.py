
count = 0

for i in range(100000):
    if i**3 % 1000 == 888:
        count += 1
        print(count, (count-1)//4, i)

